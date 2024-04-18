#set document(
     title: [Report druhého projektu ITS],
     author: "onegen",
)

#set page(
     paper: "a4",
     margin: (x: 2.3cm, y: 1.4cm),
)

#set text(
     font: "Gentium Plus",
     weight: "regular",
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

#align(center)[
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
     #align(right)[#text(size: 8pt)[`(cart.feature:2)`]]
]

#align(center)[
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
     #align(right)[#text(size: 8pt)[`(checkout.feature:1)`]]
]

#align(center)[
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
     #align(right)[#text(size: 8pt)[`(checkout.feature)`]]
]

#v(7pt)

Ve scénáři `cart.feature:1` byl odstraněn překlep a~také opakující se informace:

#align(center)[
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
]

#v(7pt)

Scénář `cart.feature:4` byl mírně přeformulován, aby byly zřetelnější kroky na
aktuálně zobrazeném produktu:

#align(center)[
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
]

#v(7pt)

Scénář `checkout.feature:1` byl upraven, aby lépe odpovídal postupu objednávání
v~systému OpenCart (oddělení personal/billing údajů,
přidán krok výběru Guest Checkout):

#align(center)[
     #grid(
          columns: (1fr, 1fr),
          align: left + horizon,
          text(size: 7pt)[
               `Given user is not logged in` \
               `When user proceeds to checkout` \
               #highlight[#sym.space.thin] \
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
]

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

Scénář `checkout.feature:1` na Docker-kontejneru druhého projektu selže.
Na rozdíl od prvního, stránka `checkout/checkout` směřuje na `checkout/cart`,
přestože košík není prázdný. Příčinu se mi nepodařilo najít. Pro jistotu je
tento scénář v odevzdané verzi přeskočen.

#align(center)[
#block()[
#align(left)[
#text(size: 7pt)[
     `Scenario: Guest Checkout` \
     `     Given user is not logged in` \
     #highlight(fill: rgb("#ff0000a1"))[
          `     When user proceeds to checkout`
     ] \
     `     And user selects guest checkout` \
     `     And user fills out personal information` \
     `     And user selects a shipping option` \
     `     And user selects a payment method` \
     `     And user confirms the order` \
     `     Then order confirmation is displayed`
]
]
]
]