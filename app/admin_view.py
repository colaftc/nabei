from flask_admin.contrib.sqla import ModelView
from .backend import backend_is_authenticated
from flask import url_for,request,redirect

class BaseModelView(ModelView):
    def is_accessible(self):
        return backend_is_authenticated()

    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('backend.login',next=request.url))

    can_view_details=True
    page_size=50
    can_export=True
    create_modal=True
    edit_modal=True
    details_modal=True

class OutsideOrderModelView(BaseModelView):
    def scaffold_list_columns(self):
        return ['products','total','order_date']

    column_searchable_list=['created','total','products']
    column_filters=['created']
    column_editable_list=['products','total']

    column_labels=dict(
        products='商品',
        total='总价',
        order_date='下单时间',
        created='创建时间',
        updated='更新时间',
    )

class ExpenditureModelView(BaseModelView):
    def scaffold_lit_columns(self):
        return ['title','price','pay_date']

    column_searchable_list=['pay_date','price','title']
    column_filters=['pay_date']
    column_editable_list=['price','title']

    column_labels=dict(
        title='名目',
        price='金额',
        pay_date='支付日期',
        created='创建时间',
        updated='更新时间',
    )

class TaskModelView(BaseModelView):
    def scaffold_list_columns(self):
        return ['content','created','urgent']

    column_searchable_list=['content']
    column_filters=['created']
    column_editable_list=['content','urgent']

    column_labels=dict(
        content='任务内容',
        urgent='是否紧急',
        created='发布时间',
    )
