from application_services.BaseApplicationResource import BaseRDBApplicationResource
from application_services.UsersResource.user_rdb_service import UserRDBService
import database_services.RDBService as d_service


class UserResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'aaaaaF21E6156', 'users'

    @classmethod
    def get_users_and_addresses(cls):
        return UserRDBService.get_user_and_address(None)
