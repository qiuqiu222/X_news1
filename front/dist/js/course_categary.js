/**
 * Created by lenovo on 2020/5/4.
 */
function Course_Categary() {

}

Course_Categary.prototype.run = function () {
    var self = this;
    self.listenAddCourseCategaryEvent();
    self.listenEditCourseCategaryEvent();
    self.listenDeleteCourseCategaryEvent();
};
Course_Categary.prototype.listenAddCourseCategaryEvent = function () {
    var addBtn = $("#add-btn");
    addBtn.click(function () {
        xfzalert.alertOneInput({
            'title':'课程分类',
            'placeholdder':'请输入分类名称',
            'confirmCallback':function (inputValue) {
                xfzajax.post({
                    'url':'/cms/add_course_categary/',
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
            }})
    })
};
Course_Categary.prototype.listenEditCourseCategaryEvent = function () {
    var editBtn = $(".edit-btn");
    editBtn.click(function () {
        var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-pk');
        var name = tr.attr('data-name');
        xfzalert.alertOneInput({
            'title':'编辑课程名称',
            'placeholder':'请输入课程名称',
            'value':name,
            'confirmCallback':function (inputValue) {
                xfzajax.post({
                    'url':'/cms/edit_course_category/',
                    'data':{
                        'name':inputValue,
                        'pk':pk
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
Course_Categary.prototype.listenDeleteCourseCategaryEvent = function (){
    var deleteBtn = $(".delete-btn")
    deleteBtn.click(function () {
        var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-pk')
        var name = tr.attr('data-name')
        xfzalert.alertConfirm({
            'title':'确定删除吗',
            'confirmCallback':function () {
                xfzajax.post({
                    'url':'/cms/delete_course_category/',
                    'data':{
                        'pk':pk
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
}
;
$(function () {
    var course_categary = new Course_Categary();
    course_categary.run();
});