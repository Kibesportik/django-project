$('.order_button').click(function (){
    const order_btn = $(this);
    const final_price = $('#final_price_'+String(order_btn.data('id')));
    const order_amount = $('#order_amount_'+String(order_btn.data('id')));
    const price = Number(order_btn.data('price'));
    order_amount.on("input", (event) => {
        let final_order_price = order_amount.val() * price;
        final_price.html(`<p>Final price: ${final_order_price} $</p>`);
    });
});

$('.final-order-btn').click(function (){
    const final_order_btn = $(this);
    const amount_input = $('#order_amount_'+String(final_order_btn.data('id'))).val()
    const modal = $('#OrderModal_'+String(final_order_btn.data('id')))
    const product_id = final_order_btn.data('id')
    $.ajax('/new-order/'+product_id+'/' ,{
        'type':'POST',
        'async': true,
        'dataType':'json',
        'data': {
        'csrfmiddlewaretoken':$('[name="csrfmiddlewaretoken"]').val(),
        'quantity' : amount_input },
        'success': function(response){
            modal.modal('hide')
        }
    });
});