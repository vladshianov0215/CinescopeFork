from Modul_4.Cinescope.enums.roles import Roles

from Modul_4.Cinescope.enums.roles import Roles

class Role:
    def __init__(self, role_id, scope="global"):
        if role_id not in Roles._value2member_map_:
            raise ValueError(f"Invalid role: {role_id}")
        self.role_id = role_id
        self.scope = scope