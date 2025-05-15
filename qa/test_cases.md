| TC\_ID | Title              | Steps                            | Expected Result                | Status |
| ------ | ------------------ | -------------------------------- | ------------------------------ | ------ |
| TC\_01 | Load homepage      | Open `/`                         | Homepage loads with title      | Pass   |
| TC\_02 | View products      | Click on "Browse Products"       | Product page displays products | Pass   |
| TC\_03 | Add to cart        | Click "Add to Cart" on Product A | Cart updated                   | Fail   |
| TC\_04 | Navigate to cart   | Click "Go to Cart"               | Cart page loads                | Pass   |
| TC\_05 | Invalid route test | Visit `/unknown`                 | 404 error page                 | Pass   |
