from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface


class CustomerDAOImp(CustomerDAOInterface):
    def insert_into_customers_table(self, customer_obj):
        pass

    def delete_from_customers_table_by_id(self, customer_id: int) -> bool:
        pass

