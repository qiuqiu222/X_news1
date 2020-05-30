function Teacher() {

}

Teacher.prototype.run = function () {
    var self = this;
    self.listenAddTeacher();
    self.listenDeleteTeacherEvent();
    self.listenEditTeacherEvent();
}

Teacher.prototype.listenAddTeacher = function () {
    var addBtn = $("#add-btn");
    addBtn.click(function () {
        xfzalert.alertOneInput({
            'title':"添加老师名称",
            'placeholder':'老师名称',
            'confirmCallback':function (inputValue) {
                xfzajax.post({
                    'url':'/cms/add_teacher/',
                    'data':{
                        'name':inputValue
                    },
                    'success':function (result) {
                        if(result['code']===200){
                            window.location.reload();
                        }else{
                            xfzalert.close();
                        }
                    }
                })
            }
        })
    })
};

Teacher.prototype.listenDeleteTeacherEvent = function () {
    var deleteBtn = $(".delete-btn");
    deleteBtn.click(function () {
        var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr("data-pk");
        xfzalert.alertConfirm({
            'title':'确定删除吗？',
            'confirmCallback':function () {
                xfzajax.post({
                    'url':'/cms/delete_teacher/',
                    'data':{
                        'pk':pk
                    },
                    'success':function (result) {
                        if(result['code']===200){
                            window.location.reload();
                        }
                    }
                })
            }
        })
    })
};

Teacher.prototype.listenEditTeacherEvent = function () {
    var editBtn = $(".edit-btn");
    editBtn.click(function () {
        var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-id');
        var name = tr.attr('data-name');
        xfzalert.alertOneInput({
            'title':'修改这个名字吗',
            'placeholder':'请输入',
            'value':name,
            'confirmCallback':function (inputValue) {
                xfzajax.post({
                    'url':'/cms/edit_teacher/',
                    'data':{
                        'pk':pk,
                        'name':inputValue
                        },
                    'success':function (result) {
                        if(result['code']===200){
                          window.location.reload();
                        }else{
                            xfzalert.close();
                        }
                    }
                })
            }
        })
    })
};
$(function () {
    var teacher = new Teacher();
    teacher.run();
});