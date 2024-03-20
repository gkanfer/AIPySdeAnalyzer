# testingg NB values
import pymc as pm
import arviz as az
x = pm.draw(pm.NegativeBinomial.dist(mu=20, alpha=1.2),draws=1500, random_seed=RANDOM_SEED)
nonz = np.count_nonzero(x.ravel())
zeo = np.size(x.ravel()) - nonz
az.plot_kde(
            x,
            plot_kwargs={"label":f'zeros: {zeo}  non zeros: {nonz}'}
        )
