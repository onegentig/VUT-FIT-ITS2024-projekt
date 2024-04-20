#set page(
     paper: "a4",
     margin: (x: 2.3cm, y: 1.4cm),
)

#set text(
     font: "Gentium Plus",
     lang: "ces",
     size: 11pt,
)

#set par(justify: true)

#let uv(body) = { text[#sym.quote.low.double#body#sym.quote.l.double] }

#align(center)[
     #grid(
          columns: (3cm, 1fr, 3cm),
          stroke: (
               top: black,
               bottom: black,
          ),
          align: center + horizon,
          image("vut_logo.svg", height: 3.4cm),
          [
               #text(17pt)[*Report druhého projektu ITS*] \
               #text(14pt)[onegen někdo (xkrame00)] \
               #text(13pt)[#datetime.today().display(
                    "[day]. [month]. [year]"
               ) v Brně]
          ],
          image("vut_logo.svg", height: 3.4cm),
     )
]

#v(0.5cm)

= Upravené testy

Z několika scénářů byly odstraněny zbytečné členy #uv[a / an / the]:

#grid(
     columns: (1fr, 1fr),
     align: left + horizon,
     text(size: 7pt)[
          `Given user is on "Monitor" category page` \
          `And store sells "Samsung SyncMaster 941BW" in "Monitor" category` \
          `When user adds "Samsung SyncMaster 941BW" to their shopping cart` \
          `Then shopping cart contains `#highlight[`a `]`"Samsung SyncMaster 941BW"`
     ],
     text(size: 7pt)[
          `Given user is on "Monitor" category page` \
          `And store sells "Samsung SyncMaster 941BW" in "Monitor" category` \
          `When user adds "Samsung SyncMaster 941BW" to their shopping cart` \
          `Then shopping cart contains `#highlight[#sym.space.thin]`"Samsung SyncMaster 941BW"`
     ],
)

#grid(
     columns: (1fr, 1fr),
     align: left + horizon,
     text(size: 7pt)[
          `Given `#highlight[`the `]`user is not logged in` \
          `When `#highlight[`the `]`user proceeds to checkout` \
          `And `#highlight[`the `]`user fills out billing and personal information` \
          `And `#highlight[`the `]`user fills out shipping information` \
          `And user selects a payment method` \
          `And `#highlight[`the `]`user confirms the order` \
          `Then order confirmation should be displayed`
     ],
     text(size: 7pt)[
          `Given `#highlight[#sym.space.thin]`user is not logged in` \
          `When `#highlight[#sym.space.thin]`user proceeds to checkout` \
          `And `#highlight[#sym.space.thin]`user fills out billing and personal information` \
          `And `#highlight[#sym.space.thin]`user fills out shipping information` \
          `And user selects a payment method` \
          `And `#highlight[#sym.space.thin]`user confirms the order` \
          `Then order confirmation should be displayed`
     ],
)

#grid(
     columns: (1fr, 1fr),
     align: left + horizon,
     text(size: 7pt)[
          `Background:` \
          `     Given `#highlight[`the `]`user’s shopping cart is not empty`
     ],
     text(size: 7pt)[
          `Background:` \
          `     Given `#highlight[#sym.space.thin]`user’s shopping cart is not empty`
     ],
)

#v(7pt)

Ve scénáři `cart.feature:1` byl odstraněn překlep a~také opakující se informace:

#grid(
     columns: (1fr, 1fr),
     align: left + horizon,
     text(size: 7pt)[
          `Given user is on the store’s homepage` \
          `And homepage features "iPhone"`#highlight[` on its homepage`] \
          `When user adds "iPhone" to their shopping cart` \
          `Then shopping cart contains `#highlight[`am `]`"iPhone"`
     ],
     text(size: 7pt)[
          `Given user is on the store’s homepage` \
          `And homepage features "iPhone"`#highlight[#sym.space.thin] \
          `When user adds "iPhone" to their shopping cart` \
          `Then shopping cart contains `#highlight[#sym.space.thin]`"iPhone"`
     ],
)

#v(7pt)

Scénář `cart.feature:4` byl mírně přeformulován, aby byly zřetelnější kroky na
aktuálně zobrazeném produktu:

#grid(
     columns: (1fr, 1fr),
     align: left + horizon,
     text(size: 7pt)[
          `Given user is on "Palm Treo Pro" product page` \
          `When user sets `#highlight[#sym.space.thin]`quantity to "3"` \
          `And user adds `#highlight[`"Palm Treo Pro"`]` to their shopping cart` \
          `Then shopping cart contains "3" "Palm Treo Pro"`
     ],
     text(size: 7pt)[
          `Given user is on "Palm Treo Pro" product page` \
          `When user sets `#highlight[`current item’s `]`quantity to "3"` \
          `And user adds `#highlight[`current item`]` to their shopping cart` \
          `Then shopping cart contains "3" "Palm Treo Pro"`
     ],
)

#v(7pt)

Scénář `checkout.feature:1` byl upraven, aby lépe odpovídal postupu objednávání
v~systému OpenCart (oddělení personal/billing údajů,
přidán krok výběru Guest Checkout):

#grid(
     columns: (1fr, 1fr),
     align: left + horizon,
     text(size: 7pt)[
          `Given user is not logged in` \
          `When user proceeds to checkout` \
          `And user fills out `#highlight[`billing and `]`personal information` \
          `And user `#highlight[`fills out`]` shipping `#highlight[`information`] \
          `And user selects a payment method` \
          `And user confirms the order` \
          `Then order confirmation `#highlight[`should be`]` displayed`
     ],
     text(size: 7pt)[
          `Given user is not logged in` \
          `When user proceeds to checkout` \
          #highlight[`And user selects guest checkout`] \
          `And user fills out `#highlight[#sym.space.thin]`personal information` \
          `And user `#highlight[`selects a`]` shipping `#highlight[`option`] \
          `And user selects a payment method` \
          `And user confirms the order` \
          `Then order confirmation `#highlight[`is`]` displayed`
     ],
)

Scénář `goods_mgmt.feature:2` byl lépe specifikován:

#grid(
     columns: (1fr, 1fr),
     align: left + top,
     text(size: 7pt)[
          ```
          Given the admin is on the product management page
          When the admin changes something about the product "Apple Cinema 30"
          Then the product "Apple Cinema 30" should be updated in the store
          ```
     ],
     text(size: 7pt)[
          ```
          Given admin is on product management page
          When admin opens product "Product 8"
          When admin renames the product to "Product 9 Pro"
          Then product "Product 9 Pro" is present in the product list
          And product "Product 8" is not present in the product list
          ```
     ],
)

#pagebreak()

= Odstraněné testy

Scénář `checkout.feature:2` je přeskočen kvůli nutnosti registrace
(je stále přítomen, ale nespustí se).

Scénář `checkout.feature:3` byl odstraněn kvůli komplikované implementaci
(`Given` vyžadoval konkrétní množství v košíku):

#align(center)[
#block()[
#align(left)[
#text(size: 7pt)[
     ```gherkin
     Scenario Outline: Shipping Cost
          Given the user is checking out with subtotal <subtotal>
          When user selects a shipping method that costs <shipping>
          Then the total cost should be <total>
     
          Examples:
               | cart    | shipping | total    |
               | 123.20  | 8.00     | 131.20   |
               | 200.00  | 5.00     | 205.00   |
     ```
]
]
]
]

= Failing testy

Scénáře na `administration` stránce někdy selžou při načtení. Z nějakého důvodu
stránka `opencart:8080/administration` někdy, zdánlivě náhodně, načte
`opencart:8080`.
