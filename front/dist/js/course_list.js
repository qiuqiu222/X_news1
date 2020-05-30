/**
 * Created by lenovo on 2020/5/6.
 */
function CourseList() {

}

CourseList.prototype.run = function () {
    var self = this;
    self.listenDeleteCourseEvent();
    self.initDataPicker();
};

CourseList.prototype.initDataPicker = function () {
    var startPicker = $("#start-picker");
    var endPicker = $("#end-picker");

    var todayDate = new Date();
    var todayStr = todayDate.getFullYear() + '/' + (todayDate.getMonth()+1) + '/' + todayDate.getDate();
    var options = {
        'showButtonPanel': true,
        'format': 'yyyy/mm/dd',
        'startDate': '2017/6/1',
        'endDate': todayStr,
        'language': 'zh-CN',
        'todayBtn': 'linked',
        'todayHighlight': true,
        'clearBtn': true,
        'autoclose': true
    };
    startPicker.datepicker(options);
    endPicker.datepicker(options);
};

CourseList.prototype.listenDeleteCourseEvent = function () {
    var deleteBtn = $(".delete-btn");
    deleteBtn.click(function () {
        var currentBtn = $(this);
        var pk = currentBtn.attr('data-course-id');
        xfzalert.alertConfirm({
            'title':"确定删除吗",
            'confirmCallback':function () {
                xfzajax.post({
                    'url':'/cms/delete_course/',
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
};

$(function () {
    var course_list = new CourseList();
    course_list.run();
})