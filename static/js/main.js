document.addEventListener("DOMContentLoaded", function () {

    // Generate lucide icons
    lucide.createIcons();

    // Here we initialize swiper js
    const swiper = new Swiper('.swiper', {
        // Optional parameters
        direction: 'horizontal',
        loop: false,

        autoplay: {
            delay: 5000,
            disableOnInteraction: true,
        },

        // If we need pagination
        pagination: {
            el: '.swiper-pagination',
            dynamicBullets: true,
        },

        // Navigation arrows
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },

        // And if we need a scrollbar
        scrollbar: {
            el: '.swiper-scrollbar',
        },
    });

    // This opens the search bar on mobile screens
    const searchToggleOpen = document.getElementById("mobile-search-open")
    const searchToggleClose = document.getElementById("mobile-search-close")
    const searchBox = document.getElementById("search-box")

    searchToggleOpen.addEventListener("click", () => {
        searchBox.style.display = "flex"
        searchToggleOpen.classList.add("hide")
        searchToggleClose.classList.remove("hide")

    })

    // This closes the search bar on mobile screens
    searchToggleClose.addEventListener("click", () => {
        searchBox.style.display = "none"
        searchToggleOpen.classList.remove("hide")
        searchToggleClose.classList.add("hide")

    })

    //This opens and closes the navbar on mobile
    const menuToggleOpen = document.getElementById('mobile-nav-open')
    const menuToggleClose = document.getElementById('mobile-nav-close')
    const mobileMenu = document.getElementById('bottom-nav')

    menuToggleClose.addEventListener("click", () => {
        mobileMenu.style.right = "-70%"
    })

    menuToggleOpen.addEventListener("click", () => {
        mobileMenu.style.right = "0"
    })


    //This hides the navbar on auth pages and hides the filter from the profile page
    let loginUrl = window.location.href.includes('login');
    let logoutUrl = window.location.href.includes('logout');
    let signupUrl = window.location.href.includes('signup');
    let resetUrl = window.location.href.includes('reset');
    let filterUrl = window.location.href.includes('profiles');
    const filter = document.getElementById('filter-nav')
    const header = document.getElementById('header')

    if (loginUrl) {
        header.classList.add("hide");
    } else if (logoutUrl) {
        header.classList.add("hide");
    } else if (signupUrl) {
        header.classList.add("hide");
    } else if (resetUrl) {
        header.classList.add("hide");
    } else if (filterUrl) {
        filter.classList.add("hide");
    }

    // Checks the url for which page we are on and adds the .active class to the link
    let homeUrl = window.location.pathname == "/";
    let shopUrl = window.location.href.includes('shop');
    let contactUrl = window.location.href.includes('contact');
    let cartUrl = window.location.href.includes('cart');
    let profileUrl = window.location.href.includes('profiles');
    let homeLink = document.getElementById('home')
    let shopLink = document.getElementById('shop')
    let contactLink = document.getElementById('contact')
    let customLink = document.getElementById('custom-shirts')
    let profileLink = document.getElementById('my-profile')
    let cartLink = document.getElementById('cart')
    let cartTotal = document.getElementById('grand-total')

    if (homeUrl) {
        homeLink.classList.add("active");
    } else if (shopUrl) {
        shopLink.classList.add("active");
    } else if (contactUrl) {
        contactLink.classList.add("active");
    } else if (contactUrl) {
        customLink.classList.add("active");
    } else if (profileUrl) {
        profileLink.classList.add("active");
        profileLink.classList.remove("text-light");
    } else if (cartUrl) {
        cartLink.classList.add("active");
        cartLink.classList.remove("text-light");
        cartTotal.classList.add("active");
        cartTotal.classList.remove("text-light");
    }

    // Increase or decrease the product quantity in the cart
    let decreaseQuantityButtons = document.querySelectorAll(".decrement-quantity");
    let increaseQuantityButtons = document.querySelectorAll(".increment-quantity");

    decreaseQuantityButtons.forEach((button, index) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();

            let itemID = button.getAttribute('data-item-id');
            let quantityCounter = document.getElementById("quantity-counter_" + itemID);
            let currentQuantity = parseInt(quantityCounter.value);

            if (currentQuantity > 1) {
                quantityCounter.value = currentQuantity - 1;
            }
        });
    });

    increaseQuantityButtons.forEach((button, index) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();

            let itemID = button.getAttribute('data-item-id');
            let quantityCounter = document.getElementById("quantity-counter_" + itemID);

            let currentQuantity = parseInt(quantityCounter.value);
            quantityCounter.value = currentQuantity + 1;
        });
    });

    let updateCartButtons = document.querySelectorAll(".update-cart-button");

    updateCartButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            let formParent = button.closest('tr');
            let form = formParent.querySelector('form');

            if (form) {
                form.submit();
            }

        });
    });

    //Delete a given item from the cart
    let deleteItemButtons = document.querySelectorAll(".delete-item-button");

    deleteItemButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            let itemID = button.getAttribute('id').split('delete-item_')[1]
            let formParent = document.getElementById("delete-item_" + itemID).closest("tr")
            let form = formParent.querySelector('form');
            let csrfToken = form.firstElementChild.getAttribute('value')
            let url = "/cart/remove/" + itemID
            let data = {
                "csrfmiddlewaretoken": csrfToken
            }

            if (confirm("Do you really want to delete this item?")) {
                txt = "Item deleted!"
                $.post(url, data)
                .done(function() {
                    location.reload()
                })
            } else {
                txt = "Item spared!"
            }
        });
    });

    // Hides messages after five seconds
    setTimeout(() => {
        const message = document.getElementById("message");
        if (message) {
            message.style.display = 'none';
        }
    }, 5000);
})