# Policy Evaluation Engine for Zero Trust Access Decisions

class PolicyEngine:
    def __init__(self, policies):
        self.policies = policies

    def evaluate(self, request):
        """Evaluate access request against policies."""
        for policy in self.policies:
            if not self.apply_policy(policy, request):
                return False
        return True

    def apply_policy(self, policy, request):
        """Apply a single policy to the request."""
        # Implement the logic to check access request against the given policy
        # Placeholder logic for demonstration purposes
        return request.get('role') in policy.get('allowed_roles', [])

# Example policies
sample_policies = [
    {'allowed_roles': ['admin', 'user']},
    {'allowed_roles': ['guest']},
]

# Example request
sample_request = {'role': 'user'}
engine = PolicyEngine(sample_policies)
access_granted = engine.evaluate(sample_request)
print('Access granted:', access_granted)