$(document).ready(function () {
    var exampleModal = document.getElementById('exampleModal');
    const input_male = $("#numberInputMale")[0];
    const input_female = $("#numberInputFemale")[0];
    const fill_attendance_button = $("#fill-attendance");
    const close_attendance_button = $("#close-attendance");
    var nameSearch = $("#nameSearch");
    const allTableRows = $('table > tbody > tr');
    var allTableNames = [];

    $(allTableRows).each(function(ind,ele){allTableNames.push(
        {
            "name":$(ele).attr('data-name'),
            "visible":true,
            "ele":ele
        })});
    
    var attendance_data = {
        id: "",
        male: 0,
        female: 0,
    }
    attachEvents();

    function fillAttendance() {
        // return;
        $.ajax({
            method: "POST",
            url: "/data/person",
            indexValue: {
                male: parseInt(JSON.parse(JSON.stringify(attendance_data.male))),
                female: parseInt(JSON.parse(JSON.stringify(attendance_data.female))),
                curEle: attendance_data.curEle
            },
            data: {
                id: attendance_data.id,
                male: attendance_data.male,
                female: attendance_data.female
            }
        })
            .done(function (msg) {
                const indexValue = this.indexValue;
                $(indexValue.curEle).attr('data-male', indexValue.male)
                $(indexValue.curEle).attr('data-female', indexValue.female)
            });
    }
    function attachEvents() {
        attachIncrementAndDecrementEvents();
        attachModalEvents()
        $(nameSearch).on('change',handleSeach);
        $("#clearInputBox").on('click',function(){
            $(nameSearch).val("");
            $(nameSearch).trigger('change');
        })
        $("#searchButton").on('click',function(){
            $(nameSearch).trigger('change');
        })
    }
    function attachModalEvents() {
        exampleModal.addEventListener('show.bs.modal', function (event) {
            var button = event.relatedTarget
            const parentTR = $(button).closest('tr');
            var modalTitle = exampleModal.querySelector('.modal-title')
            attendance_data['id'] = $(button).attr("data-id");
            attendance_data.male = $(button).attr("data-male");
            attendance_data.female = $(button).attr("data-female");
            attendance_data.curEle = button
            $(input_female).attr('value', attendance_data['female']);
            $(input_male).attr('value', attendance_data['male']);
            modalTitle.textContent =  $(parentTR).attr('data-title');
        })
        exampleModal.addEventListener('hidden.bs.modal', function (event) {
        })
        $(close_attendance_button).on('click', function () {
        })
        $(fill_attendance_button).on('click', function () {
            $(close_attendance_button).click()
            fillAttendance()
        })
    }
    function attachIncrementAndDecrementEvents() {
        $("#attendance_modal").on('click', ".increment", function (event) {
            const currentElement = $(event.target);
            const currentInputElement = $(currentElement).parent().find('input')[0];
            const curVal = $(currentInputElement).val();
            const newVal = parseInt(curVal) + 1;
            if ($(currentInputElement).attr('id') == "numberInputFemale") {
                attendance_data.female = newVal;
            } else {
                attendance_data.male = newVal;
            }
            $(currentInputElement).attr('value', newVal);
        })
        $("#attendance_modal").on('click', ".decrement", function (event) {
            const currentElement = $(event.currentTarget);
            const currentInputElement = $(currentElement).parent().find('input')[0];
            const curVal = $(currentInputElement).attr('value');
            if(curVal==0){
                return;
            }
            const newVal = parseInt(curVal) - 1;
            if ($(currentInputElement).attr('id') == "numberInputFemale") {
                attendance_data.female = newVal;
            } else {
                attendance_data.male = newVal;
            }
            $(currentInputElement).attr('value', newVal);
        })
    }
    function handleSeach(event){
        console.log(event)
        console.log($(this).val())
        const curVal = $(this).val().toLocaleLowerCase();
        if(curVal==""){
            $(allTableRows).each(function(ind,ele){
                $(ele).show();
            })
            return;    
        }
        allTableNames.forEach(function(val,ind){
            if(val['name'].includes(curVal)){
                if(!val['visible']){
                    $(val['ele']).show();
                    val['visible']=true;
                }
                // else{
                //     val['visble']=false;
                // }
            }else{
                if(val['visible']){
                    val['visible']=false;
                    $(val['ele']).hide();
                }
                // else{
                //     val['visible']=true;
                // }
            }
        })

    }
})