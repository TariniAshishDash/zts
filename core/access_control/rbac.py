class Role:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, username):
        self.username = username
        self.roles = []

    def assign_role(self, role):
        self.roles.append(role)

class Permission:
    def __init__(self, name):
        self.name = name

class AccessControl:
    def __init__(self):
        self.roles = {}
        self.permissions = {}

    def add_role(self, role):
        self.roles[role.name] = role

    def add_permission(self, permission):
        self.permissions[permission.name] = permission

    def user_has_permission(self, user, permission_name):
        # Check if user has the necessary role for the permission
        for role in user.roles:
            if self._role_has_permission(role, permission_name):
                return True
        return False

    def _role_has_permission(self, role, permission_name):
        # Logic to check if the role has the specific permission
        # This should be implemented according to the actual RBAC rules
        # For example's sake, let's say every role has all permissions
        return True

# Example usage:
if __name__ == '__main__':
    ac = AccessControl()
    admin_role = Role('admin')
    user_role = Role('user')
    ac.add_role(admin_role)
    ac.add_role(user_role)

    read_permission = Permission('read')
    write_permission = Permission('write')
    ac.add_permission(read_permission)
    ac.add_permission(write_permission)

    user = User('john_doe')
    user.assign_role(user_role)

    print(f'User has read permission: {ac.user_has_permission(user, "read")}')
    print(f'User has write permission: {ac.user_has_permission(user, "write")}')
