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

Z několika scénářů byly odstraněny neurčité členy #uv[a / an]:

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
]

#v(10pt)

Ve scénáři `cart.feature:1` byl odstraněn překlep a také opakující se informace:

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

#v(10pt)

Scénář `cart.feature:4` byl mírně přeformulován, aby byly zřetelnější kroky na
aktuálně zobrazeném produktu. Záměr tohoto scénáře se ale nezměnil.

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

= Odstraněné testy

zatím žádné

= Nově přidané testy

zatím žádné

= Nalezené chyby

zatím žádné
