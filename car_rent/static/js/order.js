$(document).ready(function () {
    $('.car').html(String(localStorage.getItem('car')))
    $('.transmission').html(localStorage.getItem('transmission'))
    $('.fuel').html(localStorage.getItem('fuel'))
    $('.price-for-day').html(`${localStorage.getItem('price')} рублей`)
    $('.days').html(`${localStorage.getItem('total_days')} дней`)
    $('.dates').html(`${localStorage.getItem('first_date')}- ${localStorage.getItem('last_date')}`)
    var total=parseInt(localStorage.getItem('total_days'))* parseInt(localStorage.getItem('price'))
    $('.all-price').html(`${total} рублей`)

    $('.hidden-input').val(`Автомобиль : ${localStorage.getItem('car')},Каробка передач : ${localStorage.getItem('transmission')},
    Тип топливо : ${localStorage.getItem('fuel')},Стоимость(за день) : ${localStorage.getItem('price')},Количество дней : ${localStorage.getItem('total_days')},
    Даты : от ${localStorage.getItem('first_date')}--- до ${localStorage.getItem('last_date')},Итоговая сумма : ${total}`)

    localStorage.clear();


     
    
    
})