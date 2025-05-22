const product_search = $('#product_search')
const product_div = document.getElementById('searched_products')
product_search.on('input', (event) => {
    $.ajax('product-search/', {
        'type':'GET',
        'async': true,
        'dataType':'json',
        'data': {
        'search_word' : product_search.val() },
        'success': function(product_list){
            if (product_search.val() != ''){
                for (let product in product_list){
                    product_div.innerHTML += `<h5><button class='my_card bg-warning order_button'  data-bs-toggle="modal"
                            data-bs-target="#OrderModal_${product_list[product]['id']}"
                            data-price="${product_list[product]['price']}"
                            data-id="${product_list[product]['id']}">
                            ${product_list[product]['name']} ${product_list[product]['price']} $
                            </button></h5>`
                }
            } else {
                product_div.innerHTML = ''
            }
        }
    });
});