![testing-header](docs/testing-files/responsive-images.png)

## COMPATIBILITY

For cross-browser compatibility the browsers Google Chrome and Firefox Developer Edition were tested. Apple devices were omitted because I don´t own any. The tests were conducted on the deployed site. For the sake of readbility and to not overwhelm readers I will include representative screenshots from the landing page, forms and the cart. All other screenshots are in the repository if the reader wishes to view them beyond assessment testing.

### CHROME:

<details>
  <summary>Landing Page Responsive</summary>
<img src="docs/testing-files/homepage-responsive/homepage-responsive-all.png" ><br>
</details>

<details>
  <summary>Contact Page Responsive</summary>
<img src="docs/testing-files/contact-page-responsive/contact-responsive-all.png" ><br>
</details>

<details>
  <summary>Cart Page Responsive</summary>
<img src="docs/testing-files/cart-page-responsive/cart-responsive-all.png" ><br>
</details>

### FIREFOX:

<details>
  <summary>Landing Page Responsive</summary>
<img src="docs/testing-files/homepage-responsive/homepage-responsive-firefox-all.png" ><br>
</details>

<details>
  <summary>Contact Page Responsive</summary>
<img src="docs/testing-files/contact-page-responsive/contact-responsive-firefox-all.png" ><br>
</details>

<details>
  <summary>Cart Page Responsive</summary>
<img src="docs/testing-files/cart-page-responsive/cart-responsive-firefox-all.png" ><br>
</details>

## AUTOMATIC TESTING

For this MVP there were no automatic tests done.

## MANUAL TESTING

NOTE: Most of the features are available to guests as well as registered users. If a feature is only for registered users it is filed under the related category, if a feature is for all users it will be filed as a guest test.

| FEATURE                                                      | ACTION                                                       | EXPECTED RESULT                                              | ACTUAL RESULT                                                | TESTED | PASSED | COMMENTS                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | ------ | ------------------------------ |
| **NAVIGATION AS GUEST**                                      |                                                              |                                                              |                                                              |        |        |                                |
| Hover effects for links                                      | hover over links                                             | links turn dark                                              | links turn dark                                              | YES    | YES    |                                |
| Hover effects for buttons                                    | hover over buttons                                           | buttons lighten up                                           | buttons lighten up                                           | YES    | YES    |                                |
| CTA hover effects                                            | hover over buttons                                           | buttons lighten up                                           | buttons lighten up                                           | YES    | YES    |                                |
| Social links hover effects                                   | hover over icons                                             | icons lighten up                                             | icons lighten up                                             | YES    | YES    |                                |
| Social links open in new tab                                 | click social icon link                                       | pages open in new tab                                        | pages open in new tab                                        | YES    | YES    |                                |
| Active State                                                 | select link                                                  | selected link turns dark                                     | selected link turns dark                                     | YES    | YES    |                                |
| Links open in same tab                                       | click link                                                   | pages open in same tab                                       | pages open in same tab                                       | YES    | YES    |                                |
| **NAVIGATION AS USER**                                       |                                                              |                                                              |                                                              |        |        |                                |
| When logged in login button changes                          | log in                                                       | log in button changes to log out                             | log in button changes to log out                             | YES    | YES    |                                |
| When logged in wishlist icon shows                           | log in                                                       | list icon shows in user nav on the left side                 | list icon shows in user nav on the left side                 | YES    | YES    |                                |
| When logged in user profile icon shows                       | log in                                                       | user icon shows in user nav on the left side                 | user icon shows in user nav on the left side                 | YES    | YES    |                                |
| When logged in register CTA disappears                       | log in                                                       | register CTA disappears                                      | register CTA disappears                                      | YES    | YES    |                                |
| **CONTACT / INQUIRIES AS GUEST**                             |                                                              |                                                              |                                                              |        |        |                                |
| Form shows placeholders marked as mandatory                  | Go to contact page                                           | mandatory placeholders have star                             | mandatory placeholders have star                             | YES    | YES    |                                |
| Form uploads without image                                   | fill form without image                                      | shows info message and uploads                               | shows info message and uploads                               | YES    | YES    |                                |
| Form uploads with image                                      | fill form with image                                         | shows success message and uploads                            | shows success message and uploads                            | YES    | YES    |                                |
| **CONTACT / INQUIRIES AS USER**                              |                                                              |                                                              |                                                              |        |        |                                |
| Form is prefilled with user data                             | log in and go to contact                                     | form shows user data                                         | form shows user data                                         | YES    | YES    |                                |
| Form uploads without image                                   | fill form without image                                      | shows info message and uploads                               | shows info message and uploads                               | YES    | YES    |                                |
| Form uploads with image                                      | fill form with image                                         | shows success message and uploads                            | shows success message and uploads                            | YES    | YES    |                                |
| **SHOP AS GUEST**                                            |                                                              |                                                              |                                                              |        |        |                                |
| Guest can view product details                               | click DETAILS on card                                        | shows details, hides to wishlist button                      | shows details, hides to wishlist button                      | YES    | YES    |                                |
| Guest can add product to cart                                | click BUY                                                    | shows success message, adds to cart                          | shows success message, adds to cart                          | YES    | YES    |                                |
| Guest can change cart quantity                               | in cart increase quantity, click UPDATE                      | Increases cart quantity and payment amount                   | Increases cart quantity and payment amount                   | YES    | YES    |                                |
| Guest can delete from cart                                   | in cart, click DELETE                                        | shows warning, deletes on confirm, shows success             | shows warning, deletes on confirm, shows success             | YES    | YES    |                                |
| Guest can add to cart from shop page                         | in shop, click BUY on card                                   | shows success message, adds to cart                          | shows success message, adds to cart                          | YES    | YES    |                                |
| **CHECKOUT AS GUEST**                                        |                                                              |                                                              |                                                              |        |        |                                |
| Form shows madatory fields with star                         | buy item, go to checkout                                     | form has star on mandatory fields                            | form has star on mandatory fields                            | YES    | YES    |                                |
| After form submit, checkout success is shown                 | finish checkout process                                      | order summary is shown                                       | order summary is shown                                       | YES    | YES    | ~~has the update_total() bug~~ |
| Register and Login buttons are shown in form                 | buy item, go to checkout                                     | buttons are shown                                            | buttons are shown                                            | YES    | YES    |                                |
| **CHECKOUT AS USER**                                         |                                                              |                                                              |                                                              |        |        |                                |
| Form is prefilled with user data                             |                                                              | user data is shown in form                                   | user data is shown in form                                   | YES    | YES    |                                |
| User can save info to profile                                | buy item, go to checkout                                     | opt-in is selected and shown                                 | opt-in is selected and shown                                 | YES    | YES    |                                |
| **WISHLIST**                                                 |                                                              |                                                              |                                                              |        |        |                                |
| User can add item to wishlist from product detail page       | go to product details, click TO WISHLIST                     | item is added, success message                               | item is added, success message                               | YES    | YES    |                                |
| User can add to cart from wishlist                           | go to wishlist, click BUY                                    | item is added, success message                               | item is added, success message                               | YES    | YES    |                                |
| User can delete item from wishlist                           | go to wishlist, click REMOVE                                 | item is removed, success message                             | item is removed, success message                             | YES    | YES    |                                |
| Wishlist checks if item is already in list                   | go to product details,add item more than once                | item is not added, info message                              | item is not added, info message                              | YES    | YES    |                                |
| **CART SECURITY**                                            |                                                              |                                                              |                                                              |        |        |                                |
| Items can not be added more than five times                  | update quantity in cart > 5                                  | item is not added, error message, quantity is set back to five | item is not added, error message, quantity is set back to five | YES    | YES    |                                |
| **USER PROFILE**                                             |                                                              |                                                              |                                                              |        |        |                                |
| form shows placeholders with stars for mandatory fields      | register, go to profile                                      | form shows placeholders with star                            | form shows placeholders with star                            | YES    | YES    |                                |
| If user has address, form is prefilled                       | register, go to profile                                      | form shows user data                                         | form shows user data                                         | YES    | YES    |                                |
| Order history shows text if it is empty                      | register, go to profile                                      | list shows text                                              | list shows text                                              | YES    | YES    |                                |
| Order history shows orders as list if orders are there, order number is link | register, go to profile                                      | list shows orders                                            | list shows orders                                            | YES    | YES    |                                |
| Click on order number shows related order and testimonial box, box is empty | register, go to profile, click order number                  | order details and testimonial box are shown                  | order details and testimonial box are shown                  | YES    | YES    |                                |
| Testimonial gets saved on submit, text above box changes     | write a testimonial                                          | success message, box is saved, text changes                  | success message, box is saved, text changes                  | YES    | YES    |                                |
| If Testimonial, content is shown and can be updated          | update existing testimonial                                  | success message, box is saved, testimonial changes           | success message, box is saved, testimonial changes           | YES    | YES    |                                |
| **GENERAL SECURITY**                                         |                                                              |                                                              |                                                              |        |        |                                |
| User wishlist must not be reachable via url                  | enter /user/wishlist in url                                  | redirect to login                                            | redirect to login                                            | YES    | YES    |                                |
| User profile must not be reachable via url                   | enter /profiles/show_user/7 in url                           | redirect to login                                            | redirect to login                                            | YES    | YES    |                                |
| User order detail must not be reachable via url              | enter /profiles/order_detail/F66D19D442F942E48C103D2A5215F4E5 in url | redirect to login                                            | redirect to login                                            | YES    | YES    |                                |

## CODE VALIDATION

### W3C VALIDATION

#### BASE HTML

<details>
  <summary>Base HTML results</summary>
<img src="docs/testing-files/nuhtml/base/base-valid.png" ><br>
</details>

#### CART HTML

<details>
  <summary>Cart HTML results</summary>
<img src="docs/testing-files/nuhtml/cart/cart-valid.png" ><br>
</details>

#### HOME HTML

<details>
  <summary>Home HTML results</summary>
<img src="docs/testing-files/nuhtml/home/home-valid.png" ><br>
</details>

#### PRIVACY HTML

<details>
  <summary>Privacy HTML results</summary>
<img src="docs/testing-files/nuhtml/privacy/privacy-valid.png" ><br>
</details>

#### SHOP HTML

<details>
  <summary>Shop HTML results</summary>
<img src="docs/testing-files/nuhtml/shop/shop-valid.png" ><br>
</details>

#### WISHLIST HTML

<details>
  <summary>Wishlist HTML results</summary>
<img src="docs/testing-files/nuhtml/wishlist/wishlist-valid.png" ><br>
</details>

***NOTE: The following screenshots contain errors either produced by django itself or by libraries like django-countries. These are not fixable for me, because I would need to change the package code which will most likely be overwritten by a future aupdate which may occur. The viable option would be to provide valid html to the developers github repository via pull request.***

#### CHECKOUT HTML

<details>
  <summary>Checkout HTML results</summary>
<img src="docs/testing-files/nuhtml/checkout/checkout-errors-django-countries.png" ><br>
</details>

<details>
  <summary>Checkout HTML error proof</summary>
<img src="docs/testing-files/nuhtml/checkout/cdjango-countries-error-proof.png" ><br>
</details>

#### CONTACT/INQUIRIES HTML

<details>
  <summary>Contact HTML results</summary>
<img src="docs/testing-files/nuhtml/contact-inquiries/contact-errors-from-django.png" ><br>
</details>

<details>
  <summary>Contact HTML error proof</summary>
<img src="docs/testing-files/nuhtml/contact-inquiries/contact-errors-from-django-proof.png" ><br>
</details>

#### PROFILE HTML

<details>
  <summary>Profile HTML results</summary>
<img src="docs/testing-files/nuhtml/profile/profile-django-errors.png" ><br>
</details>

<details>
  <summary>Profile HTML error proof</summary>
<img src="docs/testing-files/nuhtml/profile/error-proof.png" ><br>
</details>

### CSS VALIDATION

<details>
  <summary>JIGSAW CSS validation</summary>
<img src="docs/testing-files/jigsaw/jigsaw-validation.png" ><br>
</details>

<details>
  <summary>JIGSAW CSS validation warnings</summary>
<img src="docs/testing-files/jigsaw/jigsaw-swiper-warnings.png" ><br>
</details>

The CSS warnings come from Swiper included via CDN.

### JS VALIDATION

<details>
  <summary>JSHINT result for main.js</summary>
<img src="docs/testing-files/jshint/jshint-validation.png" ><br>
</details>

<details>
  <summary>JSHINT result for stripe.js</summary>
<img src="docs/testing-files/jshint/jshint-validation-stripe.png" ><br>
</details>

The warnings about unused and undefined variables come from Stripe and Swiper. They are included via CDN..

### PYTHON VALIDATION

#### CART APP

<details>
  <summary>Cart Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/cart/cart-view-validate.png" ><br>
</details>

<details>
  <summary>Cart Tools PEP8 Result</summary>
<img src="docs/testing-files/pep8/cart/cart-tools.png" ><br>
</details>

<details>
  <summary>Cart Contexts PEP8 Result</summary>
<img src="docs/testing-files/pep8/cart/cart-contexts.png" ><br>
</details>

#### CHECKOUT APP

<details>
  <summary>Checkout Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/checkout/checkout-views.png" ><br>
</details>

<details>
  <summary>Checkout Models PEP8 Result</summary>
<img src="docs/testing-files/pep8/checkout/checkout-models.png" ><br>
</details>

#### CUSTOM SHIRT APP

<details>
  <summary>Custom Shirt Models PEP8 Result</summary>
<img src="docs/testing-files/pep8/customshirt/customshirt-models.png" ><br>
</details>

<details>
  <summary>Custom Shirt Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/customshirt/customshirt-views.png" ><br>
</details>

<details>
  <summary>Custom Shirt Admin PEP8 Result</summary>
<img src="docs/testing-files/pep8/customshirt/customshirt-admin.png" ><br>
</details>

#### HOME APP

<details>
  <summary>Home Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/home/home-views.png" ><br>
</details>

#### PRODUCTS APP

<details>
  <summary>Products Models PEP8 Result</summary>
<img src="docs/testing-files/pep8/products/products-models.png" ><br>
</details>

<details>
  <summary>Products Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/products/products-views.png" ><br>
</details>

<details>
  <summary>Products Admin PEP8 Result</summary>
<img src="docs/testing-files/pep8/products/products-admin.png" ><br>
</details>

#### PROFILES APP

<details>
  <summary>Profiles Models PEP8 Result</summary>
<img src="docs/testing-files/pep8/profiles/profiles-models.png" ><br>
</details>

<details>
  <summary>Profiles Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/profiles/profiles-views.png" ><br>
</details>

<details>
  <summary>Profiles Forms PEP8 Result</summary>
<img src="docs/testing-files/pep8/profiles/profiles-forms.png" ><br>
</details>

<details>
  <summary>Profiles Admin PEP8 Result</summary>
<img src="docs/testing-files/pep8/profiles/profiles-admin.png" ><br>
</details>

#### SHOP APP

<details>
  <summary>Shop Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/shop/shop-views.png" ><br>
</details>

#### TESTIMONIAL APP

<details>
  <summary>Testimonial Models PEP8 Result</summary>
<img src="docs/testing-files/pep8/testimonial/testimonial-models.png" ><br>
</details>

<details>
  <summary>Products Forms PEP8 Result</summary>
<img src="docs/testing-files/pep8/testimonial/testimonial-forms.png" ><br>
</details>

<details>
  <summary>Products Admin PEP8 Result</summary>
<img src="docs/testing-files/pep8/testimonial/testimonial-admin.png" ><br>
</details>

#### WISHLIST APP

<details>
  <summary>Wishlist Models PEP8 Result</summary>
<img src="docs/testing-files/pep8/wishlist/wishlist-models.png" ><br>
</details>

<details>
  <summary>WishlistWishlist Views PEP8 Result</summary>
<img src="docs/testing-files/pep8/wishlist/wishlist-views.png" ><br>
</details>

### WAVE VALIDATION

<details>
  <summary>WAVE Homepage results</summary>
<img src="docs/testing-files/wave/homepage-valid.png" ><br>
</details>

<details>
  <summary>WAVE Shop-Page results</summary>
<img src="docs/testing-files/wave/shop-valid.png" ><br>
</details>

<details>
  <summary>WAVE Privacy results</summary>
<img src="docs/testing-files/wave/privacy-valid.png" ><br>
</details>

<details>
  <summary>WAVE Cart results</summary>
<img src="docs/testing-files/wave/cart-valid.png" ><br>
</details>

<details>
  <summary>WAVE Custom Shirt results</summary>
<img src="docs/testing-files/wave/customshirt-valid.png" ><br>
</details>

### LIGHTHOUSE TESTS

<details>
  <summary>Lighthouse Homepage Result Desktop</summary>
<img src="docs/testing-files/lighthouse/lighthouse-desktop.png" ><br>
</details>

## BUGS

- ~~A very bad bug which I can not solve for now is that the update_total() function from the walkthrough works only in the cart. The function is returning NULL on save and reverts back to its default value of 0. I could not find out why this is happening. You can reproduce this by deleting the `default=0` attribute from the Order model and trying to save an order. The error will show the issue. However, this needs to be fixed urgently.~~
  - **This issue was fixed by changing the `self.save()` method to `super().save()` and adding the tax field to the database. Upon order completion all relevant data is saved to the database and gets displayed in the checkout success summary.**

- A smaller bug is that the filter links arent colored when they are clicked. This is happening because the main.js function handling the coloring is an if/else block checking the URL. This can be solved by adding a different visual marker. Due to time constraints this couldnt be implemented.

