$(function () {
    $('.gallery').gallery();
});
var main_date = new Array()
var a = 1
var price =parseInt(document.querySelector('.price-count').innerHTML)
$(function () {
    console.log('okkkkkkkk');
    $('.calender').pignoseCalender({
        multiple: true,
        select: function (date, obj) {
            obj.calender.parent().next().show().text('You selected ' +
                (date[0] === null ? 'null' : date[0].format('YYYY-MM-DD')) +
                '~' +
                (date[1] === null ? 'null' : date[1].format('YYYY-MM-DD')) +
                '.');
              
                a = Math.ceil((date[1]._d - date[0]._d)/(60*60*24*1000))
                
                    price =parseInt(document.querySelector('.price-count').innerHTML)
                    $('.price-value').html(`${price * a} руб. `)
                    $('.count-of-days').html(`${a} дней`)
                main_date = []
                main_date.push(date[0].format('YYYY-MM-DD'))
                main_date.push(date[1].format('YYYY-MM-DD'))
                // document.querySelector('.reserve-button').forEach(function(e){
                //     e.href = e.href +'&first_date='+date[0].format('YYYY-MM-DD')+'&second_date='+date[1].format('YYYY-MM-DD')+'&total_days='+a
                    
                // })
        }
       
    });
    
});
$(document).on("mousemove", 'body', function () {
    var car = $('.room-type').html()
    var fuel = $('.fuel-type').html()
    var car_class = $('.car-class').html()
    var transmission = $('.transmission').html()
    
    localStorage.setItem('car', JSON.stringify(car));
    localStorage.setItem('car-class', JSON.stringify(car_class));
    localStorage.setItem('fuel', JSON.stringify(fuel));
    localStorage.setItem('price', JSON.stringify(price));
    localStorage.setItem('transmission', JSON.stringify(transmission));
    if (main_date[0]){
        localStorage.setItem('first_date', JSON.stringify(main_date[0]));
    }
    else{
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();

        today = dd + '/' + mm + '/' + yyyy;
        var ds = String(parseInt(dd) + 1);
        tomorrow = ds + '/' + mm + '/' + yyyy;
        localStorage.setItem('first_date', JSON.stringify(today));
        localStorage.setItem('last_date', JSON.stringify(tomorrow));
    }
    if (main_date[1]){
        localStorage.setItem('last_date', JSON.stringify(main_date[1]));
    }

    localStorage.setItem('total_days', JSON.stringify(a));
})
