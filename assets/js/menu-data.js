window.HAVEN_MENU = {
  venue: {
    name: "Haven Cafe",
    arabicName: "هيفن",
    location: "Osara, Salalah"
  },
  categories: [
    {
      id: "signature",
      name: "Haven Favourites",
      arabicName: "مفضلات هيفن",
      description: "The drinks guests return to, led by Haven's own recipes.",
      arabicDescription: "مشروبات يختارها ضيوفنا مرارا، وفي مقدمتها ابتكارات هيفن.",
      items: [
        {
          id: "spanish-latte-hot",
          name: "Spanish Latte",
          arabicName: "سبانش لاتيه",
          description: "Espresso and milk with a measured sweetness.",
          arabicDescription: "إسبريسو وحليب بحلاوة متوازنة.",
          price: 1.7,
          largePrice: 2,
          tags: ["Hot"],
          label: "Most Ordered",
          arabicLabel: "الأكثر طلبا",
          image: "assets/img/spanish-latte.png",
          featured: true
        },
        {
          id: "spanish-latte-iced",
          name: "Iced Spanish Latte",
          arabicName: "سبانش لاتيه مثلج",
          description: "Espresso, cold milk and a measured sweetness over ice.",
          arabicDescription: "إسبريسو وحليب بارد بحلاوة متوازنة فوق الثلج.",
          price: 1.7,
          tags: ["Iced"],
          label: "Most Ordered",
          arabicLabel: "الأكثر طلبا",
          image: "assets/img/spanish-latte.png",
          featured: true
        },
        {
          id: "haven-cold-brew",
          name: "Haven Passion Fruit Cold Brew",
          arabicName: "كولد برو هيفن بالباشن فروت",
          description: "Our founding barista's recipe: slow-steeped coffee with a bright passion fruit finish.",
          arabicDescription: "وصفة ابتكرها باريستا هيفن المؤسس: قهوة منقوعة على البارد بنهاية منعشة من الباشن فروت.",
          price: 2.4,
          tags: ["Iced"],
          label: "Haven Signature",
          arabicLabel: "ابتكار هيفن",
          featured: true
        }
      ]
    },
    {
      id: "coffee-with-milk",
      name: "Coffee With Milk",
      arabicName: "قهوة بالحليب",
      description: "Espresso drinks shaped by the amount and texture of milk.",
      arabicDescription: "مشروبات إسبريسو تختلف بكمية الحليب وقوامه.",
      items: [
        {
          id: "latte-hot",
          name: "Latte",
          arabicName: "لاتيه",
          description: "Espresso softened by steamed milk.",
          arabicDescription: "إسبريسو يخففه الحليب المبخر.",
          price: 1.5,
          largePrice: 1.7,
          tags: ["Hot"]
        },
        {
          id: "latte-iced",
          name: "Iced Latte",
          arabicName: "لاتيه مثلج",
          description: "Espresso and cold milk over ice.",
          arabicDescription: "إسبريسو وحليب بارد فوق الثلج.",
          price: 1.5,
          tags: ["Iced"]
        },
        {
          id: "caramel-latte-hot",
          name: "Caramel Latte",
          arabicName: "كراميل لاتيه",
          description: "Espresso and milk with caramel sweetness.",
          arabicDescription: "إسبريسو وحليب بحلاوة الكراميل.",
          price: 1.7,
          largePrice: 1.9,
          tags: ["Hot"]
        },
        {
          id: "caramel-latte-iced",
          name: "Iced Caramel Latte",
          arabicName: "كراميل لاتيه مثلج",
          description: "Cold milk and espresso with caramel over ice.",
          arabicDescription: "حليب بارد وإسبريسو وكراميل فوق الثلج.",
          price: 1.7,
          tags: ["Iced"]
        },
        {
          id: "hazelnut-latte-hot",
          name: "Hazelnut Latte",
          arabicName: "هزلنت لاتيه",
          description: "Espresso and milk with a roasted hazelnut note.",
          arabicDescription: "إسبريسو وحليب بلمسة بندق محمص.",
          price: 1.5,
          largePrice: 1.7,
          tags: ["Hot"]
        },
        {
          id: "hazelnut-latte-iced",
          name: "Iced Hazelnut Latte",
          arabicName: "هزلنت لاتيه مثلج",
          description: "Cold milk and espresso with hazelnut over ice.",
          arabicDescription: "حليب بارد وإسبريسو وبندق فوق الثلج.",
          price: 1.5,
          tags: ["Iced"]
        },
        {
          id: "cappuccino-hot",
          name: "Cappuccino",
          arabicName: "كابتشينو",
          description: "Espresso and steamed milk under a deeper cap of foam.",
          arabicDescription: "إسبريسو وحليب مبخر تعلوهما طبقة أوفر من الرغوة.",
          price: 1.5,
          largePrice: 1.7,
          tags: ["Hot"]
        },
        {
          id: "cappuccino-iced",
          name: "Iced Cappuccino",
          arabicName: "كابتشينو مثلج",
          description: "Chilled espresso and milk with a light foam.",
          arabicDescription: "إسبريسو وحليب بارد مع رغوة خفيفة.",
          price: 1.5,
          tags: ["Iced"]
        },
        {
          id: "flat-white",
          name: "Flat White",
          arabicName: "فلات وايت",
          description: "Espresso with finely textured milk and less foam.",
          arabicDescription: "إسبريسو بحليب ناعم ورغوة أقل.",
          price: 1.6,
          tags: ["Hot"],
          image: "assets/img/hot-coffee.png"
        },
        {
          id: "cortado",
          name: "Cortado",
          arabicName: "كورتادو",
          description: "Espresso tempered with a small pour of warm milk.",
          arabicDescription: "إسبريسو مع كمية صغيرة من الحليب الدافئ.",
          price: 1.4,
          tags: ["Hot"]
        },
        {
          id: "macchiato",
          name: "Macchiato",
          arabicName: "ماكياتو",
          description: "Espresso marked with a spoonful of milk foam.",
          arabicDescription: "إسبريسو مع ملعقة من رغوة الحليب.",
          price: 1.6,
          tags: ["Hot"]
        }
      ]
    },
    {
      id: "black-coffee",
      name: "Black Coffee",
      arabicName: "قهوة سوداء",
      description: "Espresso and hand-poured coffee without milk.",
      arabicDescription: "إسبريسو وقهوة مقطرة يدويا من دون حليب.",
      items: [
        {
          id: "v60-classic-hot",
          name: "V60 Classic",
          arabicName: "في 60 كلاسيك",
          description: "Hand-poured filter coffee with a clear aroma and light body.",
          arabicDescription: "قهوة مقطرة يدويا برائحة واضحة وقوام خفيف.",
          price: 2,
          largePrice: 2.2,
          tags: ["Hot"],
          image: "assets/img/v60.png"
        },
        {
          id: "v60-classic-iced",
          name: "V60 on Ice",
          arabicName: "في 60 على الثلج",
          description: "Hand-poured coffee cooled over ice for a lighter finish.",
          arabicDescription: "قهوة مقطرة يدويا تبرد فوق الثلج بنهاية أخف.",
          price: 2,
          tags: ["Iced"]
        },
        {
          id: "v60-passion-fruit-hot",
          name: "V60 Passion Fruit",
          arabicName: "في 60 باشن فروت",
          description: "Hand-poured coffee with passion fruit adding a tart, fragrant edge.",
          arabicDescription: "قهوة مقطرة يدويا مع باشن فروت يضيف حموضة عطرية.",
          price: 2.2,
          largePrice: 2.4,
          tags: ["Hot"]
        },
        {
          id: "v60-passion-fruit-iced",
          name: "Passion Fruit V60 on Ice",
          arabicName: "في 60 باشن فروت على الثلج",
          description: "Filter coffee and passion fruit cooled over ice.",
          arabicDescription: "قهوة مقطرة وباشن فروت تبرد فوق الثلج.",
          price: 2.2,
          tags: ["Iced"]
        },
        {
          id: "americano-hot",
          name: "Americano",
          arabicName: "أمريكانو",
          description: "Espresso lengthened with hot water for a clean, direct cup.",
          arabicDescription: "إسبريسو مع ماء ساخن لكوب واضح ومباشر.",
          price: 1.3,
          largePrice: 1.5,
          tags: ["Hot"]
        },
        {
          id: "americano-iced",
          name: "Americano on Ice",
          arabicName: "أمريكانو على الثلج",
          description: "Espresso poured over cold water and ice; clear and lightly bitter.",
          arabicDescription: "إسبريسو فوق ماء بارد وثلج، واضح بمرارة خفيفة.",
          price: 1.3,
          tags: ["Iced"]
        },
        {
          id: "espresso",
          name: "Espresso",
          arabicName: "إسبريسو",
          description: "A short, concentrated cup with a lasting coffee finish.",
          arabicDescription: "كوب قصير ومركز بنهاية قهوة تدوم.",
          price: 1,
          largePrice: 1.2,
          tags: ["Hot"]
        },
        {
          id: "classic-cold-brew",
          name: "Classic Cold Brew",
          arabicName: "كولد برو كلاسيك",
          description: "Coffee steeped slowly and served cold, with a deep, direct finish.",
          arabicDescription: "قهوة منقوعة ببطء وتقدم باردة بنهاية عميقة وواضحة.",
          price: 1.8,
          tags: ["Iced"]
        }
      ]
    },
    {
      id: "chocolate-and-specials",
      name: "Chocolate & Specials",
      arabicName: "الشوكولاتة والمشروبات الخاصة",
      description: "Chocolate, matcha and espresso served with more texture.",
      arabicDescription: "مشروبات بالشوكولاتة والماتشا والإسبريسو بقوام أوضح.",
      items: [
        {
          id: "dark-mocha-hot",
          name: "Dark Mocha",
          arabicName: "دارك موكا",
          description: "Espresso and milk with the firmer cocoa edge of dark chocolate.",
          arabicDescription: "إسبريسو وحليب بطعم الكاكاو الأوضح في الشوكولاتة الداكنة.",
          price: 1.7,
          largePrice: 1.9,
          tags: ["Hot"]
        },
        {
          id: "dark-mocha-iced",
          name: "Iced Dark Mocha",
          arabicName: "دارك موكا مثلج",
          description: "Dark chocolate, cold milk and espresso over ice.",
          arabicDescription: "شوكولاتة داكنة وحليب بارد وإسبريسو فوق الثلج.",
          price: 1.7,
          tags: ["Iced"]
        },
        {
          id: "white-mocha-hot",
          name: "White Mocha",
          arabicName: "وايت موكا",
          description: "Espresso and milk with soft white-chocolate sweetness.",
          arabicDescription: "إسبريسو وحليب بحلاوة الشوكولاتة البيضاء.",
          price: 1.8,
          largePrice: 2,
          tags: ["Hot"]
        },
        {
          id: "white-mocha-iced",
          name: "Iced White Mocha",
          arabicName: "وايت موكا مثلج",
          description: "White chocolate, cold milk and espresso over ice.",
          arabicDescription: "شوكولاتة بيضاء وحليب بارد وإسبريسو فوق الثلج.",
          price: 1.7,
          tags: ["Iced"]
        },
        {
          id: "hot-chocolate",
          name: "Hot Chocolate",
          arabicName: "هوت شوكليت",
          description: "Milk and chocolate with a full, even texture.",
          arabicDescription: "حليب وشوكولاتة بقوام غني ومتجانس.",
          price: 1.5,
          largePrice: 1.7,
          tags: ["Hot"]
        },
        {
          id: "matcha-iced",
          name: "Iced Matcha",
          arabicName: "ماتشا مثلجة",
          description: "Matcha and cold milk over ice, with a clean green-tea finish.",
          arabicDescription: "ماتشا وحليب بارد فوق الثلج بنهاية واضحة من الشاي الأخضر.",
          price: 2,
          tags: ["Iced"],
          image: "assets/img/haven-matcha-real.jpg",
          featured: true
        },
        {
          id: "creamy-espresso",
          name: "Creamy Espresso",
          arabicName: "إسبريسو كريمي",
          description: "Chilled espresso blended to a thicker, creamier texture.",
          arabicDescription: "إسبريسو بارد ممزوج لقوام أكثر كثافة وكريمية.",
          price: 1.7,
          tags: ["Iced"]
        },
        {
          id: "affogato",
          name: "Affogato",
          arabicName: "أفوغاتو",
          description: "Vanilla ice cream with hot espresso poured over; cold, bitter and sweet in each spoon.",
          arabicDescription: "آيس كريم فانيلا ينساب فوقه إسبريسو ساخن؛ بارد ومر وحلو في كل ملعقة.",
          price: 1.4,
          tags: ["Iced"]
        }
      ]
    },
    {
      id: "tea",
      name: "Tea & Karkade",
      arabicName: "الشاي والكركديه",
      description: "Hot tea, chilled hibiscus and fruit iced teas.",
      arabicDescription: "شاي ساخن وكركديه بارد وآيس تي بالفواكه.",
      items: [
        {
          id: "black-tea",
          name: "Black Tea",
          arabicName: "شاي أسود",
          description: "Black tea served hot and unadorned.",
          arabicDescription: "شاي أسود يقدم ساخنا من دون إضافات.",
          price: 0.5,
          tags: ["Hot"]
        },
        {
          id: "tea-milk",
          name: "Tea With Milk",
          arabicName: "شاي بالحليب",
          description: "Hot black tea rounded with milk.",
          arabicDescription: "شاي أسود ساخن يلينه الحليب.",
          price: 0.7,
          tags: ["Hot"]
        },
        {
          id: "karkade",
          name: "Karkade",
          arabicName: "كركديه",
          description: "Chilled hibiscus with a tart, berry-like taste.",
          arabicDescription: "كركديه بارد بطعم لاذع يشبه التوت.",
          price: 1.5,
          tags: ["Iced"],
          image: "assets/img/haven-karkade-real.jpg"
        },
        {
          id: "passion-fruit-iced-tea",
          name: "Passion Fruit Iced Tea",
          arabicName: "آيس تي باشن فروت",
          description: "Cold tea with the tart fragrance of passion fruit.",
          arabicDescription: "شاي بارد برائحة الباشن فروت وحموضته الخفيفة.",
          price: 1.3,
          tags: ["Iced"]
        },
        {
          id: "mango-iced-tea",
          name: "Mango Iced Tea",
          arabicName: "آيس تي مانجو",
          description: "Cold tea with ripe mango sweetness.",
          arabicDescription: "شاي بارد بحلاوة المانجو الناضجة.",
          price: 1.3,
          tags: ["Iced"]
        },
        {
          id: "peach-iced-tea",
          name: "Peach Iced Tea",
          arabicName: "آيس تي خوخ",
          description: "Cold tea with a soft peach finish.",
          arabicDescription: "شاي بارد بنهاية ناعمة من الخوخ.",
          price: 1.3,
          tags: ["Iced"]
        }
      ]
    },
    {
      id: "smoothies-and-shakes",
      name: "Smoothies & Shakes",
      arabicName: "سموذي وميلك شيك",
      description: "Cold fruit blends and milkshakes.",
      arabicDescription: "خلطات فواكه باردة وميلك شيك.",
      items: [
        {
          id: "acai-smoothie",
          name: "Açaí Smoothie",
          arabicName: "سموذي أساي",
          description: "A cold açaí blend with a tart dark-berry taste.",
          arabicDescription: "خليط أساي بارد بطعم التوت الداكن والحامض.",
          price: 1.8,
          tags: ["Iced"]
        },
        {
          id: "strawberry-smoothie",
          name: "Strawberry Smoothie",
          arabicName: "سموذي فراولة",
          description: "Strawberry blended cold to a thick, even texture.",
          arabicDescription: "فراولة ممزوجة باردة بقوام كثيف ومتجانس.",
          price: 1.8,
          tags: ["Iced"]
        },
        {
          id: "pistachio-milkshake",
          name: "Pistachio Milkshake",
          arabicName: "ميلك شيك فستق",
          description: "A thick milkshake with the roasted taste of pistachio.",
          arabicDescription: "ميلك شيك كثيف بطعم الفستق المحمص.",
          price: 1.8,
          tags: ["Iced"],
          image: "assets/img/milkshakes.png"
        },
        {
          id: "mango-milkshake",
          name: "Mango Milkshake",
          arabicName: "ميلك شيك مانجو",
          description: "A thick milkshake with ripe mango sweetness.",
          arabicDescription: "ميلك شيك كثيف بحلاوة المانجو الناضجة.",
          price: 1.8,
          tags: ["Iced"]
        }
      ]
    },
    {
      id: "mojitos",
      name: "Mojitos",
      arabicName: "موهيتو",
      description: "Fruit, mint and citrus served over ice.",
      arabicDescription: "فواكه ونعناع وحمضيات تقدم فوق الثلج.",
      items: [
        {
          id: "strawberry-mojito",
          name: "Strawberry Mojito",
          arabicName: "موهيتو فراولة",
          description: "Strawberry, mint and citrus over ice.",
          arabicDescription: "فراولة ونعناع وحمضيات فوق الثلج.",
          price: 1.4,
          tags: ["Iced"]
        },
        {
          id: "blueberry-mojito",
          name: "Blueberry Mojito",
          arabicName: "موهيتو بلوبيري",
          description: "Blueberry, mint and citrus over ice.",
          arabicDescription: "بلوبيري ونعناع وحمضيات فوق الثلج.",
          price: 1.4,
          tags: ["Iced"],
          image: "assets/img/mojito-blueberry.png"
        },
        {
          id: "passion-fruit-mojito",
          name: "Passion Fruit Mojito",
          arabicName: "موهيتو باشن فروت",
          description: "Passion fruit, mint and citrus over ice.",
          arabicDescription: "باشن فروت ونعناع وحمضيات فوق الثلج.",
          price: 1.4,
          tags: ["Iced"]
        },
        {
          id: "peach-mojito",
          name: "Peach Mojito",
          arabicName: "موهيتو خوخ",
          description: "Peach, mint and citrus over ice.",
          arabicDescription: "خوخ ونعناع وحمضيات فوق الثلج.",
          price: 1.4,
          tags: ["Iced"]
        }
      ]
    },
    {
      id: "water",
      name: "Water",
      arabicName: "المياه",
      description: "Still water served chilled.",
      arabicDescription: "مياه طبيعية تقدم باردة.",
      items: [
        {
          id: "still-water",
          name: "Still Water",
          arabicName: "مياه طبيعية",
          description: "Chilled still water.",
          arabicDescription: "مياه طبيعية باردة.",
          price: 0.2,
          tags: ["Iced"]
        }
      ]
    },
    {
      id: "desserts",
      name: "Sweets & Cakes",
      arabicName: "الحلويات والكيك",
      description: "Four desserts chosen to sit naturally beside coffee.",
      arabicDescription: "أربع حلويات مختارة لترافق القهوة.",
      items: [
        {
          id: "truffle-mango",
          name: "Truffle Mango",
          arabicName: "ترافل مانجو",
          description: "Mango and cream in soft, chilled layers.",
          arabicDescription: "مانجو وكريمة في طبقات باردة وناعمة.",
          price: 2.5,
          tags: ["Dessert"]
        },
        {
          id: "brownie",
          name: "Brownie",
          arabicName: "براوني",
          description: "A dense chocolate crumb with a soft centre.",
          arabicDescription: "قوام شوكولاتة كثيف بقلب طري.",
          price: 2.3,
          tags: ["Dessert"],
          image: "assets/img/brownie.png",
          featured: true
        },
        {
          id: "san-sebastian",
          name: "San Sebastian Cheesecake",
          arabicName: "تشيز كيك سان سيباستيان",
          description: "Basque-style cheesecake with a browned top and soft centre.",
          arabicDescription: "تشيز كيك باسكي بسطح محمر وقلب طري.",
          price: 1.5,
          tags: ["Dessert"]
        },
        {
          id: "chocolate-cheesecake",
          name: "Chocolate Cheesecake",
          arabicName: "تشيز كيك شوكولاتة",
          description: "Chocolate cheesecake with a dense, creamy centre.",
          arabicDescription: "تشيز كيك بالشوكولاتة وقلب كثيف وكريمي.",
          price: 1.5,
          tags: ["Dessert"]
        }
      ]
    }
  ]
};
