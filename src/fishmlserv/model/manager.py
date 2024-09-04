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

fish_model = None

def pp(l, w):
    global fish_model

    if fish_model is None
        # 로드
        pkl = get_model_path()
        with open(pkl, "rb") as f:
            fish_model = pickle.load(f)

    prediction = fish_model.predict([[length, weight]])

    fish_class = "빙어"
    if prediction[0] == 1:
        fish_class = "도미"

    return {
                "prediction": fish_class,
                "length": length,
                "weight": weight
            }
