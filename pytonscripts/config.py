class Config:
    def __init__(self, env):
        SUPPORTED_ENVS =['test','pre','prod']
       

        self.base_url = {
            'test':'http://172.29.90.230',
            'pre':'http://172.29.46.11',
            'prod':'https://shufersal.verifone.co.il/'
            }[env]
        self.web_port = {
            'test':'80',
            'pre':'80',
            'prod':'443'    
            }[env]