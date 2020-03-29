# python里的orm框架
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = "user"

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

if __name__ == "__main__":
    # 初始化数据库连接:
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/myshop')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    new_user = User(id="2",name="wp")
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    user = session.query(User).filter(User.id=="1").one()
    print(user)
    session.close()

