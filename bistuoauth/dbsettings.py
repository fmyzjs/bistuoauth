#!-*- coding=utf-8 -*-
class appdb(object):

    def db_for_read(self, model, **hints):
        #该方法定义读取时从哪一个数据库读取
		return self.__app_router(model)

    def db_for_write(self, model, **hints):
        #该方法定义写入时从哪一个数据库读取，如果读写分离，可再额外配置
        return 'default'

    def allow_syncdb(self, db, model):
        #该方法定义数据库是否能和名为db的数据库同步
        return self.__app_router(model) == db

   #添加一个私有方法用来判断模型属于哪个应用，并返回应该使用的数据库
    def __app_router(self, model):
        if model._meta.app_label == 'bistu_member':
            return 'bistu_member'
        else :
            return 'default'