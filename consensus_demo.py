import random

# Proof of Work Simulation
miner1 = {'name': 'MinerA', 'power': random.randint(1, 100)}
miner2 = {'name': 'MinerB', 'power': random.randint(1, 100)}

selected_pow = max([miner1, miner2], key=lambda x: x['power'])
print(f"[PoW] Selected: {selected_pow['name']} with power {selected_pow['power']}")

# Proof of Stake Simulation
staker1 = {'name': 'StakerA', 'stake': random.randint(100, 1000)}
staker2 = {'name': 'StakerB', 'stake': random.randint(100, 1000)}

selected_pos = max([staker1, staker2], key=lambda x: x['stake'])
print(f"[PoS] Selected: {selected_pos['name']} with stake {selected_pos['stake']}")

# Delegated Proof of Stake Simulation
voters = ['User1', 'User2', 'User3']
delegates = ['DelegateA', 'DelegateB']

votes = {'DelegateA': 0, 'DelegateB': 0}

for voter in voters:
    vote = random.choice(delegates)
    votes[vote] += 1

selected_dpos = max(votes, key=votes.get)
print(f"[DPoS] Selected: {selected_dpos} with {votes[selected_dpos]} votes")
