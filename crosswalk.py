from rllab.algos.trpo import TRPO
from rllab.baselines.linear_feature_baseline import LinearFeatureBaseline
from rllab.baselines.zero_baseline import ZeroBaseline
from rllab.envs.crosswalk_env import CrosswalkEnv
from rllab.envs.normalized_env import normalize
from rllab.policies.gaussian_mlp_policy import GaussianMLPPolicy

env = normalize(CrosswalkEnv())
policy = GaussianMLPPolicy(env_spec=env.spec,
                           hidden_sizes=(512, 256, 128, 64, 32))
baseline = LinearFeatureBaseline(env_spec=env.spec)
algo = TRPO(
    env=env,
    policy=policy,
    baseline=LinearFeatureBaseline(env_spec=env.spec),
    batch_size=4000,
    step_size=0.01,
    n_itr=500
)
algo.train()