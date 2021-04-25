
const all_data = {

}

$(document).on('change', '.for-selection', function () {
    var marka_id = $('.for-selection').find('option:selected').val()
    
    console.log(marka_id)
    $.ajax({
        url: '/api/v1.0/cars/models/',
        method: "GET",
        data: {
            'marka_id': marka_id,
        },
        success: function (data) {
            $('.model-select').html('')
            for (model of data.models) {
            
            $('.model-select').append(`<option class="text-white bg-primary model" value="${model.id}">${model.model}</option>`)
        }
    }
    });

});
$(document).on('change', '.model-select', function () {
    var model_id = $('.model-select').find('option:selected').val()
    all_data['model_id'] = model_id
    loadAllData(all_data)

});

document.querySelector('.min-price').addEventListener('input', (e) => {
    var minPrice = document.querySelector('.min-price').value
    all_data['minPrice'] = minPrice
    loadAllData(all_data)
})
document.querySelector('.max-price').addEventListener('input', (e) => {
    var maxPrice = document.querySelector('.max-price').value
    all_data['maxPrice'] = maxPrice
    loadAllData(all_data)
})

document.onclick = function (e) {
    if (e.target.classList.contains('checked-inputs')) {

        document.querySelectorAll('.checked-inputs').forEach(function (e) {
            if (e.classList.contains('types')) {
                if (e.checked == true) {
                    var checked_status = e.closest('.ally').querySelector('.choose-types').innerText
                    all_data['checked_status'] = checked_status
                    console.log(checked_status)
                    loadAllData(all_data)
                    
                }
            }
            if (e.classList.contains('feature') && e.checked == true) {
                var checked_class = e.closest('.ally').querySelector('.choose-types').innerText
                all_data['checked_class'] = checked_class
                loadAllData(all_data)
            }

        })
    }
}



function loadAllData(data) {
    console.log(data)
    $.ajax({
        url: 'http://34.69.142.55/api/v1.0/cars/cars/',
        method: "GET",
        data: data,
        success: function (response) {
            console.log(response)
            document.querySelector('.removed-data').innerHTML = ''
            // console.log(response.page_range)
            for (car of response.filtered_cars) {
                document.querySelector('.removed-data').innerHTML +=`
                <div class="row main-div">
                <div class="col-12 ">
                    <div class="card mb-3 p-3"
                        style="max-width: 100%; height: 90%;border-color: #5bbaff;box-shadow: 0 0 10px #5bbaff;background-color: #ebf3ff;">
                        <div class="row no-gutters">
                            <div class="col-md-4 col-sm-6 col-lg-3 col-12">
                                <img class="content-image card-img" src="${car.main_image}">
                            </div>
                            <div class="col-md-4 col-sm-6 col-lg-6 col-12">
                                <div class="card-body">
                                    <h6 class="card-title text-primary mb-1" style="font-weight: bold;">
                                    ${car.marka.marka} ${car.model.model} (${car.fuel.name})</h6>
                                    <div class="d-flex align-items-center mb-3 ">
                                    </div>
                                    <p class="card-text" style="font-size: 12px;line-height: 18px;">
                                    ${car.car_year.year} model car</p>
                                    <p class="card-text"><small class="text-muted">Best car</small>
                                    </p>
                                    <span class="d-sm-block d-md-none" style="font-size: 16px;">Price
                                        for night
                                        ${car.price} руб.</span>
                                </div>
                            </div>
                            <div class="col-md-4 col-sm-6 col-lg-3 d-none d-md-block col-12">
                                <div class="row flex-column justify-content-between h-100 ">
                                    
                                    <div class=" d-flex flex-column justify-content-end h-100 px-2">
                                  
                                        <span class="text-right mb-2" style="font-size: 16px;">Price for night
                                        ${car.price} руб.</span>
                                            <a href="car-detail/${car.id}" type="button"
                                            class="btn btn-danger slugs-anchor"
                                            style="font-size:14px; color: white;">Арендовать</a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 p-sm-3  pb-4 pl-4 d-block d-sm-none ">
                                <div class="row  ">
                                    <a href="car-detail/${car.id}" type="button" class="btn btn-danger slugs-anchor w-25"
                                        style="font-size:14px; color: white;">Арендовать</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
               `
            }
            document.querySelector('.old-pagi').innerHTML=''
            document.querySelector('.js-pagination').innerHTML=''
            for (var i =1;i<=response.page_range;i++){
                page_numbers=document.createElement('span')
                page_numbers.innerText=i
                page_numbers.href=`?page=${i}`
                document.querySelector('.js-pagination').appendChild(page_numbers)
                page_numbers.classList.add('m-2','pagination-numbers-js')

                page_numbers.addEventListener('click',function(){
                    all_data['page']=this.innerText
                    loadAllData(all_data)
                })
            }
            
        },
        error: function (error) {
            console.log(error)
        }
    })
}