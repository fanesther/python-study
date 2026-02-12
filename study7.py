# %%
import pyro


# %% Ice Cream Sale Example
def weather():
    cloudy = pyro.sample(
        "cloudy", pyro.distributions.Bernoulli(0.3)
    )  # p

    # if cloudy.item() == 1.0:
    #     cloudy = "cloudy"
    # else:
    #     cloudy = "sunny"

    cloudy = "cloudy" if cloudy.item() == 1.0 else "sunny"

    mean_temp = {"cloudy": 55.0, "sunny": 75.0}[cloudy]
    scale_temp = {"cloudy": 10.0, "sunny": 15.0}[cloudy]
    temp = pyro.sample(
        "temp", pyro.distributions.Normal(mean_temp, scale_temp)
    )
    return cloudy, temp.item()


# %%
for _ in range(10):
    print(weather())


# %% Ice Cream Sale Example cont'd
def ice_cream_sales():
    cloudy, temp = weather()

    if cloudy == "sunny" and temp > 80.0:
        expected_sales = 200.0
    else:
        expected_sales = 50.0

    ice_cream = pyro.sample(
        "ice_cream", pyro.distributions.Normal(expected_sales, 10.0)
    )
    return ice_cream.item()


for _ in range(3):
    print(ice_cream_sales())


# %% Sample by tensor
import pyro
import torch


# %%
def test_func(a, b, c):
    return a + b + c


print(test_func(1, 2, 3))

arguments = [10, 20, 30]
print(test_func(arguments[0],arguments[1],arguments[2]))
print(test_func(*arguments))

invalid_arguments = [10, 20]
print(test_func(*invalid_arguments))

# %%
dict_arguments = {}
for key in ["a", "b", "c"]:
    dict_arguments[key] = 5

print(test_func(**dict_arguments))


# %%
def weathers(n):
    cloudys = pyro.sample(
        "cloudy", pyro.distributions.Bernoulli(0.3 * torch.ones(n))
    )

    def _cloudy(tensor):
        return "cloudy" if tensor.item() == 1.0 else "sunny"

    def _mean_scale(tensor):
        cloudy = _cloudy(tensor)
        mean_temp = {"cloudy": 55.0, "sunny": 75.0}[cloudy]
        scale_temp = {"cloudy": 10.0, "sunny": 15.0}[cloudy]
        return mean_temp, scale_temp

    def _get_distribution(tensor):
        return pyro.sample(
            "temp", pyro.distributions.Normal(*_mean_scale(tensor))
        )

    temps = [
        (_cloudy(tensor), _get_distribution(tensor).item())
        for tensor in cloudys
    ]
    return temps


from pprint import pprint


pprint(weathers(5))

# %%
print(weathers(5))

# %% Monte Carlo
import pyro
import seaborn as sns
import torch
import matplotlib.pyplot as plt
from pyro.infer.mcmc import HMC, MCMC


def model():
    # Observations are binary observations which come
    # from a Bernoulli distribution with some percent
    # "p" to be correct and (1-p) of being wrong
    # To estimate that p value, we start not knowing
    # anything about it, so our prior will be
    # a uniform distribution from 0.0 to 1.0
    underlying_p = pyro.sample(
        "p", pyro.distributions.Uniform(0.0, 1.0)
    )
    y_hidden_dist = pyro.distributions.Bernoulli(underlying_p)
    y_real = pyro.sample("obs", y_hidden_dist)
    return y_real


def conditioned_model(model, y):
    conditioned_model_function = pyro.poutine.condition(
        model, data={"obs": y}
    )
    return conditioned_model_function()


def monte_carlo(y):
    pyro.clear_param_store()
    hmc_kernel = HMC(conditioned_model, step_size=0.1)
    mcmc = MCMC(hmc_kernel, num_samples=500, warmup_steps=100)
    mcmc.run(model, y)
    sample_dict = mcmc.get_samples(num_samples=5000)
    plt.figure(figsize=(8, 6))
    sns.distplot(sample_dict["p"].numpy())
    plt.xlabel("Observed probability value")
    plt.ylabel("Observed frequency")
    plt.show()
    mcmc.summary(prob=0.95)
    return sample_dict


y = pyro.distributions.Bernoulli(0.4 * torch.ones(100))()
monte_carlo(y)

# %%
y.sum()

# %%
