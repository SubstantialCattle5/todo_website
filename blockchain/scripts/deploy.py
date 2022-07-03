from brownie import User , accounts , config , network
from scripts.common import get_account
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]

def user_deploy() :
    account = get_account()
    main_deploy = User.deploy({
        "from" : account
    })
    flag = main_deploy.signup('a' , 'b' , {
          'from' : account })
    print(f"Sign up was {flag}")

    a , b = main_deploy.recover(account)
    print(f"Username :{a}\nPassword :{b}")

    logged =  main_deploy.login('b' , {
        "from" : account
    })
    exist , logged_id  = logged.return_value
    print(f"{exist} {logged_id}")


def main() :
    user_deploy()