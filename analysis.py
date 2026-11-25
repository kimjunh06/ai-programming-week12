import pandas as pd


def 정제(df):
    df = df.copy()  
    print("시작        ", len(df))

    df = df.dropna(subset=["점수"])
    print("빈 칸 제거  ", len(df))


    df = df.drop_duplicates()
    print("중복 제거   ", len(df))
    
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()
    
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))
    return df


def 반별평균(df):
    
    표 = df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]).round(2)
    print(표)
    
    return 표["mean"]


if __name__ == "__main__":
    df = 정제(pd.read_csv("scores_2026.csv"))

    
    수학 = df[df["과목"] == "수학"]
    print("수학 행 수:", len(수학))
    print("1반 & 90점 이상:", len(df[(df["반"] == "1반") & (df["점수"] >= 90)]))

    
    print(df.groupby("반")["점수"].mean().round(2))
    print(df.groupby(["과목", "반"])["점수"].mean().round(2))

    반별평균(df)