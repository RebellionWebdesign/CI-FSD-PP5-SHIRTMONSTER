/*
The documentation for this part can be found here:
https://stripe.com/docs/payments/accept-a-payment

CSS is from here:
https://stripe.com/docs/stripe.js
*/

/*
Copied from the walkthrough. The stripe documentation
recommends the payment element now and doesnt provide information on
the card element anymore.
*/
var stripePublicKey = $('#id_stripePublicKey').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: 'white',
        fontFamily: '"poppins", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Card element error handler
card.addEventListener("change", function (event) {
    var errorDiv = document.getElementById("card-errors")
    if (event.error) {
        var html = 
            `<p>${event.error.message}</p>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
})

// Form submission handler
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#stripe-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = 
                `<p>${result.error.message}</p>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#stripe-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});