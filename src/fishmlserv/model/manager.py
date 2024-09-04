def get_model_path():
    """
    import os
    이 함수 파일의 절대 경로를 받아온다.
    절대 경로를 이용해 model.pkl 의 경로를 조합
    조합된 경로를 리턴하면 끝

    사용 fastapi main.py 에서 아래와 같이 사용
    from fishmlserv.model.manager import get_model_path
    """
    import os
    file = __file__
    sp_file = file.split("/")
    pkl_pwd = "/".join(sp_file[:-1]) + "/model.pkl"
    return pkl_pwd

