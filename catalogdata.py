#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import Base, Category, Guitar

print "\n\n------------------------\nWorking...\n\n"

print "==> Establishing database link..."
engine = create_engine('sqlite:///gtrcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

print "    Database connection established."
print "==> Adding items to database..."

# Add Categories
gtrcat1 = Category(name="Classical Guitars",
                   description="Wooden nylon-string acoustic guitars for classical concert, orchestral, and chamber music.",
                   color="maroon")
session.add(gtrcat1)

gtrcat2 = Category(name="Steel-String Acoustic Guitars",
                   description="Modern wooden steel-string acoustic guitars.",
                   color="saddlebrown")
session.add(gtrcat2)

gtrcat3 = Category(name="Electric Guitars",
                   description="Steel-string guitars with higher string action and electromagnetic pickups, for use with amps.",
                   color="midnightblue")
session.add(gtrcat3)

gtrcat4 = Category(name="Electro-Acoustic Guitars",
                   description="Hybrid acoustic guitars with electric pickups.",
                   color="indigo")
session.add(gtrcat4)

gtrcat5 = Category(name="Twelve-String Guitars",
                   description="Modern steel-string acoustic guitars with 12 strings, typically used as rhythm instruments.",
                   color="darkolivegreen")
session.add(gtrcat5)

gtrcat6 = Category(name="Resonator Guitars",
                   description="Steel-string guitars with a resonator plate, usually played Dobro-style, with a slide.",
                   color="slategray")
session.add(gtrcat6)

gtrcat7 = Category(name="Steel Lap Guitars",
                   description="Lap steel guitars (often called Hawaiian guitars) played with pedals and metal slide.",
                   color="darkgreen")
session.add(gtrcat7)

gtrcat8 = Category(name="Electric Bass Guitars",
                   description="Four-string electric guitars with lower range and darker timbre, typically used as a rhythm instrument.",
                   color="darkslategray")
session.add(gtrcat8)

gtrcat9 = Category(name="Double-Neck Guitars",
                   description="Wh-who... who even plays these things?!",
                   color="deeppink")
session.add(gtrcat9)

session.commit()


# Add Classical Guitars
gtr_cls_1 = Guitar(name="Cordoba C5",
                   description="The Cordoba C5 Classical Guitar is perfect for any aspiring classical guitarist or steel-string/electric wizard looking to take a walk on the wild nylon-string side. The solid cedar top produces an amazingly rich tone while the wide string placement, easy string tension, and low action make it a breeze to play. The C5 comes with mahogany back and sides and a Spanish cedar neck.",
                   slug="cordoba_c5",
                   views=232,
                   category=gtrcat1)

gtr_cls_2 = Guitar(name="Yamaha C40",
                   description="The Yamaha C40 PKG is an attractive package for beginners, featuring the full-size C40 nylon-string classical guitar along with a digital tuner, instructional DVD, and a gig bag for safe storage and transport. The C40 guitar features a spruce top with meranti back and sides, a nato neck with a rosewood fretboard, rosewood bridge, and a gloss finish. It is designed to serve as an affordable, yet high-quality, full-size starter guitar.",
                   slug="yamaha_c40",
                   views=458,
                   category=gtrcat1)

gtr_cls_3 = Guitar(name="Lucero LC100",
                   description="Nicely made with a laminated spruce top, mahogany body, and rosewood fingerboard and bridge.  Natural gloss finish. The Lucero LC100 Classical Guitar features a laminated spruce top and mahogany back and sides. An excellent guitar for the beginner.",
                   slug="lucero_lc100",
                   views=91,
                   category=gtrcat1)

gtr_cls_4 = Guitar(name="Cordoba 45MR",
                   description="The Cordoba 45MR CD/MR nylon-string acoustic guitar is a handmade traditional acoustic guitar featuring a solid cedar top with Madagascar rosewood back and sides, an ebony fingerboard, a Spanish neck heel joint that provides instrument strength and doesn't lose any tone. The guitar's High-gloss PU finish lets the wood's beauty shine through for all to admire.",
                   slug="cordoba_45mr",
                   views=186,
                   category=gtrcat1)

gtr_cls_5 = Guitar(name="Kremona Sofia",
                   description="The Kremona Sofia is crafted from highly sustainable West African sapele, offering tonal vibrancy and balance. A red cedar top adds warmth and articulation to Sofia's lyrical timbre. Specifications include solid matte back and sides, solid gloss top, African mahogany neck, adjustable truss rod, Indian rosewood fingerboard, bridge and headstock overlay, bone nut and saddle, wood binding and rosette, gold machines with amber buttons, 650 mm scale length, 52mm neck width at nut, and Kremona Arete medium-high tension strings.",
                   slug="kremona_sofia",
                   views=208,
                   category=gtrcat1)

session.add(gtr_cls_1)
session.add(gtr_cls_2)
session.add(gtr_cls_3)
session.add(gtr_cls_4)
session.add(gtr_cls_5)
session.commit()


# Add Modern Acoustic Guitars
gtr_acs_1 = Guitar(name="Taylor 114ce",
                   description="This cutaway acoustic/electric Grand Auditorium blends layered walnut back and sides with a solid Sitka spruce top, making it a great all-around acoustic that responds well to strumming, flatpicking and fingerpicking. Enjoy the easier playability and accurate intonation with slightly narrower 1-11/16-inch nut width that makes forming barre chords easier on the hands.",
                   slug="taylor_114ce",
                   views=1853,
                   category=gtrcat2)

gtr_acs_2 = Guitar(name="Martin DC-16GTE",
                   description="The DC-16GTE acoustic-electric guitar features a D-14 platform and a Dreadnought cutaway body design equipped with balanced tonewoods that produce a rich acoustic tone for recording or live performance. The sapele back and sides complement the solid Sitka spruce top finished in a polished gloss.",
                   slug="martin_dc16gte",
                   views=1103,
                   category=gtrcat2)

gtr_acs_3 = Guitar(name="Takamine P3DC",
                   description="The P3DC cutaway dreadnought features resonant tonewoods, elegant appointments and state-of-the-art electronics that deliver an exquisite acoustic experience onstage and off. Other premium features include a solid sapele back, mahogany neck, rosewood fingerboard with wood dot-in-dot inlays, gold tuners with amber buttons, natural satin finish, and the highly acclaimed CT4B II preamp system with three-band EQ, volume control and built-in tuner.",
                   slug="takamine_p3dc",
                   views=985,
                   category=gtrcat2)

gtr_acs_4 = Guitar(name="Fender CD-60S",
                   description="Fender's redesigned CD-60S features a solid spruce top, mahogany back and sides, a mahogany neck with a comfortable easy-to-play profile, and a smooth rosewood fingerboard with rolled edges. This instrument's large dreadnought body size and classic tonewoods deliver a huge, full-bodied sound with ample projection for vocal accompaniment, solo work, and many other unplugged or live applications.",
                   slug="fender_cd60s",
                   views=851,
                   category=gtrcat2)

gtr_acs_5 = Guitar(name="Fender FA-100",
                   description="This instrument features a protective and glossy finish encompassing the body, time tested quartersawn X bracing, a compensated saddle and laminated Spruce top. This popular budget-conscious acoustic delivers much of the tone that you'd get from more expensive instruments.",
                   slug="fender_fa100",
                   views=1550,
                   category=gtrcat2)

gtr_acs_6 = Guitar(name="Alvarez AF30",
                   description="The Folk body shape of the AF30 has impressive projection for its size. Its tone is enhanced with advanced scalloped bracing and other premium components such as bone saddles and nuts and a bi-level rosewood bridge. The sound is warm, open and powerful, and both the treble and bass registers are clearly present and balanced in relation to each other.",
                   slug="alvarez_af30",
                   views=344,
                   category=gtrcat2)

gtr_acs_7 = Guitar(name="Yamaha LS6",
                   description="The Yamaha LS6 handcrafted acoustic guitar features a grand auditorium sized body that is small and yet deep enough to deliver excellent volume that cannot normally be found in a compact body. Handcrafted with a solid Englemann Spruce top, the LS6 offers an incredible experience in total exuberance.",
                   slug="yamaha_ls6",
                   views=562,
                   category=gtrcat2)

gtr_acs_8 = Guitar(name="Seagull S6",
                   description="Wild cherry back and sides provide a unique tone on this S6 Original from Seagull, blending the warmth of mahogany with the crisp definition of maple. Silverleaf maple neck with a rosewood fretboard is easy on the fingers, while specially aligned machine heads make for quick, stable tuning.",
                   slug="seagull_s6",
                   views=705,
                   category=gtrcat2)

gtr_acs_9 = Guitar(name="Blueridge BR-70",
                   description="With exquisite Santos rosewood back and sides, and a full D-41 style abalone trim, this dreadnought faithfully delivers solid, classic tone with a sharp modern look. Expertly applied white binding adorns the body, neck, and headstock. The abalone and pearl inlay work on the headstock and the back center stripe of intricate wood marquetry are touches of fine art. Aged-tone finish completes the look. The slim mahogany neck and traditional dreadnaught body make it a truly enjoyable guitar to play.",
                   slug="blueridge_br70",
                   views=522,
                   category=gtrcat2)

session.add(gtr_acs_1)
session.add(gtr_acs_2)
session.add(gtr_acs_3)
session.add(gtr_acs_4)
session.add(gtr_acs_5)
session.add(gtr_acs_6)
session.add(gtr_acs_7)
session.add(gtr_acs_8)
session.add(gtr_acs_9)
session.commit()


# Add Electric Guitars
gtr_elc_1 = Guitar(name="Epiphone Les Paul Standard",
                   description="The mahogany body of the Les Paul Standard provides superb resonance while the Alnico Classic humbucker pickups deliver loads of warmth. The set mahogany neck with slim-tapered profile and rosewood fretboard give you the familiar feel and fast action that Les Paul players love so dearly. Neck and body binding and trapezoid inlays produce the classic look seen on stages around the world for decades. The LockTone Tune-O-Matic bridge and stopbar tailpiece provide more sustain and make string changing easier.",
                   slug="epiphone_lespaulstd",
                   views=3055,
                   category=gtrcat3)

gtr_elc_2 = Guitar(name="Fender American Stratocaster",
                   description="This latest iteration of the time-honored classic is the very essence of Strat tone and remains a beauty to see, hear and feel. Features include hand-rolled fingerboard edges, classic 50s pickups, staggered tuners, improved bridge with bent steel saddles and copper-infused high-mass block for increased resonance and sustain, tinted neck, high-gloss maple fretboard, satin neck back for smooth playability, and thin-finish undercoat that lets the body breathe and improves resonance.",
                   slug="fender_stratocaster",
                   views=3212,
                   category=gtrcat3)

gtr_elc_3 = Guitar(name="PRS S2 Custom 24",
                   description="The PRS S2 Custom 24 solidbody electric guitar's comfortable asymmetric bevel-cut double-cutaway body is built from maple-topped mahogany, so it's loaded with warmth, resonance, and copious amounts of bite and sustain. Instill your playing with incredible vintage sweetness, clarity, and extended tonal range, courtesy of the PRS S2 Custom 24's upgraded 85/15 S humbuckers. This guitar's Pattern Regular neck features an extended 24-fret rosewood fingerboard that makes high-register soloing easy.",
                   slug="prs_s2custom24",
                   views=1812,
                   category=gtrcat3)

gtr_elc_4 = Guitar(name="Shecter Hellraiser C-1",
                   description="Featuring the tried-and-true combination of a mahogany body and a quilted maple top, the Hellraiser C-1 sports a big midrange with a sweet top end. All of this tonal muscle is pushed through your amp by an EMG 81TW at the bridge with an EMG 89 at the neck. The 81TW's dual-mode design gives you the classic EMG 81 sound with the addition of a single-coil sound and a fatter tone with punch and clarity.Other cool features on the Hellraiser C-1 include a 3-piece mahogany neck for awesome stability, a TonePros TOM bridge with through-body construction, and Schecter locking tuners to keep you in tune.",
                   slug="shecter_hellraiserc1",
                   views=1255,
                   category=gtrcat3)

gtr_elc_5 = Guitar(name="Gibson Flying V 120",
                   description="The Flying V is the original rabble-rousing rocker, way ahead of its time in the late 50s and still a major style statement today. Combining time-tested tonewoods, versatile pickups, and unparalleled craftsmanship at an unbeatable price, the Flying V 120 launches your music into the stratosphere, while making the perfect ticket to the party for collector and player alike.",
                   slug="gibson_flyingv120",
                   views=1240,
                   category=gtrcat3)

gtr_elc_6 = Guitar(name="B.C. Rich MK5 Warlock",
                   description="This unique model is brought to bear with classic electronic layout: Twin covered high output B.C.Rich pickups, each with an individual Volume and Tone control and Master 3 way pickup selector give Mk5 Warlock a familiar feel and control while delivering pure, bewitching tones.",
                   slug="bcrich_mk5warlock",
                   views=769,
                   category=gtrcat3)

gtr_elc_7 = Guitar(name="ESP LTD Elite Eclipse-1",
                   description="This solidbody electric guitar is features a single-cutaway body made from mahogany topped with flame maple, giving the Elite Eclipse-I the same tonal foundation as some of the most-played guitars in rock. Top-notch touches like the Gotoh Magnum Lock tuners and Gotoh TOM bridge/tailpiece provide performance you can count on day in, day out. Factor in a tone-packed pair of Seymour Duncan humbucking pickups, and you've got a ton of potential.",
                   slug="esp_eclipse1",
                   views=941,
                   category=gtrcat3)

gtr_elc_8 = Guitar(name="Fender Standard Telecaster",
                   description="The Standard Telecaster features the best of the old and the new: a fast-action gloss maple neck, cast/sealed machine heads, 2 classic single-coil pickups, and a 6-saddle string-thru-body bridge. Since its introduction in the early '50s, guitarists in all musical genres have relied on the Fender Telecaster guitar for its timeless, powerful tone and smooth playability.",
                   slug="fender_telecaster",
                   views=2984,
                   category=gtrcat3)

gtr_elc_9 = Guitar(name="Yamaha PAC112V",
                   description="With solid alder body and pro-level hardware and electronics, this electric guitar is well known for great tone and outstanding playability. It features a comfort-contoured body, bolt-on neck design, vintage-style vibratos, and 5-way switching of the H-S-S pickup configuration. And, to top it off, it's an amazing value in its price range.",
                   slug="yamaha_pac112v",
                   views=2510,
                   category=gtrcat3)

gtr_elc_10 = Guitar(name="Ibanez RG450DX",
                   description="The RG450DX comes with a super-resonant, lightweight, and balanced mahogany body. This made-for-metal beast also boasts a 3-piece Wizard III neck that's ultra fast and eminently shreddable. For tonal diversity, the RG450DX slams with two humbucking pickups and a single-coil squarely in the middle. If you want an axe that's built for speed, the Ibanez RG450DX belongs in your hands and plugged into your amp.",
                   slug="ibanez_rg450dx",
                   views=1012,
                   category=gtrcat3)

gtr_elc_11 = Guitar(name="Oscar Schmidt OE30",
                   description="From volume and tone controls to the fully adjustable truss rods, this guitar as a whole is even greater than its many great parts. The dot inlay and stop tailpiece combine with a rosewood fingerboard and twin Washburn HH pickups to provide an excellent playground for processing musical ideas from your mind to your fingers to the strings.",
                   slug="oscarschmidt_oe30",
                   views=584,
                   category=gtrcat3)

session.add(gtr_elc_1)
session.add(gtr_elc_2)
session.add(gtr_elc_3)
session.add(gtr_elc_4)
session.add(gtr_elc_5)
session.add(gtr_elc_6)
session.add(gtr_elc_7)
session.add(gtr_elc_8)
session.add(gtr_elc_9)
session.add(gtr_elc_10)
session.add(gtr_elc_11)
session.commit()


# Add Electro-Acoustic Guitars
gtr_eac_1 = Guitar(name="Fender FA135CE",
                   description="With laminated spruce top, basswood back and sides, and Fishman ION-T preamp system, the Fender FA-135CE is built on the concert-style platform for a sleek, modern design. The laminated spruce top features X-bracing for bright, punchy tone, ideal for lead guitar. The neck is nato, and the back and sides are laminated basswood-both tone woods known for letting the mid and high frequencies sing out.",
                   slug="fender_fa135ce",
                   views=600,
                   category=gtrcat4)

gtr_eac_2 = Guitar(name="Epiphone Hummingbird Pro",
                   description="This 6-string acoustic-electric guitar is instantly recognizable, both in look and its warm sound. The Hummingbird Pro features a solid spruce top, a mahogany body, and a mahogany neck for pure tone. What's more, a distinctive hummingbird pickguard sets off the body while beautiful, split parallelogram inlays give the rosewood fingerboard an elegance all its own.",
                   slug="epiphone_hummingbird",
                   views=712,
                   category=gtrcat4)

gtr_eac_3 = Guitar(name="Kona K2",
                   description="The Kona K2 Series Natural Gloss Thin Body Electric Acoustic Guitars strike the balance between the low profile electric guitar feel, and the acoustic guitar tone. This guitar is the perfect crossover instrument for the electric guitarists looking for a true, balanced acoustic sound without large body adjustment, or the smaller player that is uncomfortable with the deep dreadnought stretch.",
                   slug="kona_k2",
                   views=513,
                   category=gtrcat4)

gtr_eac_4 = Guitar(name="Ibanez V70CE",
                   description="The V70CE's high-quality electronics and select spruce top deliver articulate amplified tone. It features a rosewood fretboard, chrome tuners, mahogany neck, back, and sides. The V70CE is equipped with a soft cutaway for higher access and is a very responsive instrument with capacity for great dynamic range both acoustically and through the output.",
                   slug="ibanez_v70ce",
                   views=455,
                   category=gtrcat4)

gtr_eac_5 = Guitar(name="Yamaha APX500III Thinline",
                   description="The  APX600 is a thinline acoustic-electric guitar, with a thinner profile that fits up close to your body, so it's easy and comfortable to play. It features a spruce top, a nato body and neck, and rosewood fingerboard and bridge that combine to put out a superior, far-reaching tone. It comes with a built-in tuner and a System 65A preamp piezo pickup system, great for plugging in and playing coffeehouse gigs with a natural acoustic sound.",
                   slug="yamaha_apx500iii",
                   views=206,
                   category=gtrcat4)

session.add(gtr_eac_1)
session.add(gtr_eac_2)
session.add(gtr_eac_3)
session.add(gtr_eac_4)
session.add(gtr_eac_5)
session.commit()


# Add Twelve-String Guitars
gtr_tst_1 = Guitar(name="Takamine EF381SC",
                   description="The versatility of this 12-string guitar begins with its solid cedar top that can play sweet mellow passages or power chords with equal ability. The onboard CT4B II preamp system (with three-band EQ, volume control and built-in tuner), paired with the unique Palathetic under-saddle pickup, provide peerless amplified response.",
                   slug="takamine_ef381sc12",
                   views=255,
                   category=gtrcat5)

gtr_tst_2 = Guitar(name="Martin D12x1ae",
                   description="The Martin D12X1AE acoustic-electric 12-string guitar adds a modern flair to a classic instrument. With its onboard Fishman Sonitone electronics, this versatile 12-string guitar projects the full, robust sound that can fill the room. The D12X1AE's mahogany grained HPL on the back and sides reflects Martin's environmentally friendly mindset. You'll love the warm, classic tones you hear as you play this modern guitar.",
                   slug="martin_d12x1ae",
                   views=382,
                   category=gtrcat5)

gtr_tst_3 = Guitar(name="Yamaha FG820-12",
                   description="Yamaha's 12 string acoustic model, with simple and traditional looks and outstanding quality, at an affordable price. It's a solid-top guitar with an authentic sound that is well balanced without sacrificing its robust strength, thanks to the newly developed scalloped bracing design. In addition to warmer and stronger sound, the body binding and fingerboard binding are cream plastic, for an upgraded look.",
                   slug="yamaha_fg82012",
                   views=533,
                   category=gtrcat5)

gtr_tst_4 = Guitar(name="Gretsch G5422TG-12",
                   description="Profoundly stylish, the G5422TG offers full hollow-body build and electrifying authenticity with Filter Tron humbucking pickups, versatile upgraded controls, oversized bound F holes, aged multi-ply body binding, smaller late- 50s G6120 bound headstock, Graph Tech NuBone nut, pearloid Neo-Classic thumbnail fingerboard inlays and a gold Bigsby B60 vibrato tailpiece.",
                   slug="gretsch_g5422tg12",
                   views=259,
                   category=gtrcat5)

gtr_tst_5 = Guitar(name="Ibanez AS7312 Artcore",
                   description="The AS7312 features an all-maple body, set-neck construction, and a pair of ART humbucking pickups. The Artcore's combination of quality workmanship and affordability has created legions of fans from diverse genres as blues, country, rock and jazz. Musicians can find the purity of an old school style jazz-box to a hybrid semi-hollow rocker.",
                   slug="ibanez_as7312artcore",
                   views=448,
                   category=gtrcat5)

gtr_tst_6 = Guitar(name="Epiphone DR-212",
                   description="The DR-212 features a select spruce top with scalloped bracing and features a mahogany body and a mahogany neck to balance its strong voice with warmth. With its blend of quality woods and superb tone, Epiphone DR-212 is the perfect first 12-string guitar. And thanks to its affordable price, that signature 12-string sound doesn't have to be out of reach.",
                   slug="epiphone_dr212",
                   views=206,
                   category=gtrcat5)

session.add(gtr_tst_1)
session.add(gtr_tst_2)
session.add(gtr_tst_3)
session.add(gtr_tst_4)
session.add(gtr_tst_5)
session.add(gtr_tst_6)
session.commit()


# Add Resonator Guitars
gtr_rsn_1 = Guitar(name="Gretsch G9200",
                   description="The Gretsch G9200 Roundneck Boxcar standard resonator guitar gives you a whole new tonal palette. The G9200 sports a mahogany top, body, and neck; a rosewood fingerboard; and Gretsch's hand-spun Ampli-Sonic spider cone and bridge - all working in concert to serve up authentic resonator tone. You'll find this great-sounding resonator as easy to play as any other guitar.",
                   slug="gretsch_g9200",
                   views=156,
                   category=gtrcat6)

gtr_rsn_2 = Guitar(name="Gold Tone PBS-D",
                   description="Designed by legendary maker Paul Beard, the Gold Tone Paul Beard Square Neck Deluxe (PBS-D) signature model guitar is hand made and provides unmatched tone in its price range. The PBS-D features an ebony fingerboard, maple back and sides, and a high gloss tobacco sunburst finish.",
                   slug="goldtone_pbsd",
                   views=269,
                   category=gtrcat6)

gtr_rsn_3 = Guitar(name="Rogue Classic Spider Resonator",
                   description="The Classic Spider's die-cast spider bridge and 10.5-inch spun aluminum resonator cone give it exceptional projection and volume. It's constructed with a spruce top; mahogany back, sides, and neck; and rosewood fretboard. Mother-of-pearl diamond fretboard inlays, a chromeplated bell, and brass coverplate and tailpiece give it authentic looks.",
                   slug="rogue_spiderres",
                   views=251,
                   category=gtrcat6)

gtr_rsn_4 = Guitar(name="Dean Resonator Heirloom",
                   description="The newest addition to Dean Guitars' line of resonators, the Heirloom is made of solid distressed copper or solid distressed brass with matching inlays and truss rod cover. Each Heirloom has a unique voice and a truly one-of-a-kind look and feel and unique distressed characteristics such as stains in the finish.",
                   slug="dean_resheirloom",
                   views=402,
                   category=gtrcat6)

gtr_rsn_5 = Guitar(name="Regal RC-55",
                   description="The new RC-50 features a brass body with an antiqued nickel finish and distinctive tone - ideal for the blues and Hawaiian music - and a volume and carrying power that has to be heard to be believed!",
                   slug="regal_rc55",
                   views=366,
                   category=gtrcat6)

session.add(gtr_rsn_1)
session.add(gtr_rsn_2)
session.add(gtr_rsn_3)
session.add(gtr_rsn_4)
session.add(gtr_rsn_5)
session.commit()


# Add Steel Lap Guitars
gtr_stl_1 = Guitar(name="Morrell JMPTB-6",
                   description="The JMPTB-6 steel lap guitar is loaded with a Kent Armstrong HR1R Hot Rails hum cancelling pickup. This is a dual blade mini humbucker is designed for high gain applications with emphasis on bass and midrange frequencies. The maple body yields greater sustain and volume projection while the poplar body ads warmth to the sound.",
                   slug="morrell_jmptb6",
                   views=399,
                   category=gtrcat7)

gtr_stl_2 = Guitar(name="Rogue RLS-1",
                   description="Slide into some classic country, Hawaiian, and blues tones with the affordable Rogue RLS1 Lap Steel Guitar. It features a hardwood body and neck with position markers, a single-coil pickup, volume and tone controls, chrome hardware, and a stainless steel pickguard.",
                   slug="rogue_rls1",
                   views=176,
                   category=gtrcat7)

gtr_stl_3 = Guitar(name="Gretsch G5700 Electromatic Lap",
                   description="The G5700 is a value-packed proposition with a solid mahogany body for vibrant, wide ranging tone, and chrome hardware. The Gretsch single-coil pickup puts out lucidly smooth sounds with just the right amount of bite and jangle.",
                   slug="gretsch_electromaticlap",
                   views=279,
                   category=gtrcat7)

gtr_stl_4 = Guitar(name="Epiphone Electar",
                   description="The Electar is a reissue of one of the company's most popular vintage designs, with 1-piece mahogany body, Circus Tent control knobs, traditional fretboard markings, and vintage-style metal Epiphone headstock badge. You'll also love the modern conveniences built in, such as a powerful Epiphone 500B Blade humbucking pickup and inset non-slip rubber pads.",
                   slug="epiphone_electar",
                   views=224,
                   category=gtrcat7)

gtr_stl_5 = Guitar(name="Imperial Royal Hawaiian Teardrop",
                   description="This limited-edition lap guitar returns with luxurious features, such as Solid Sapele Mahogany top, back and sides, Fishman Sonicore pickup with Presys preamp system, on-board tuner and notch filter, rosewood fingerboard with inlaid diamond pearl position markers.",
                   slug="imperial_rhteardrop",
                   views=251,
                   category=gtrcat7)

gtr_stl_6 = Guitar(name="Gold Tone LM Weissenborn",
                   description="The Weissenborn Hawaiian steel, a platapus among guitars to the uninitiated, is an instrument brilliantly and specifically conceived for Hawaiian playing. These hollow-neck Hawaiians are enjoying a renaissance with players nearly 60 years after the last one was made. Many session pros now routinely carry along a Weissenborn for steel or Dobro calls.",
                   slug="goldtone_weissenborn",
                   views=357,
                   category=gtrcat7)

session.add(gtr_stl_1)
session.add(gtr_stl_2)
session.add(gtr_stl_3)
session.add(gtr_stl_4)
session.add(gtr_stl_5)
session.add(gtr_stl_6)
session.commit()


# Add Electric Bass Guitars
gtr_bas_1 = Guitar(name="Fender Standard Precision Bass",
                   description="Combining traditional design with contemporary features, the Standard Precision Bass is an elegant and affordable classic designed for the bassist who appreciates great style, rich and muscular tone, and excellent value. Time-honored Fender style and performance-minded modern upgrades don't have to break the bank, and this model delivers the best of both in a design ideal for Precision Bass players everywhere at every level.",
                   slug="fender_pbass",
                   views=2328,
                   category=gtrcat8)

gtr_bas_2 = Guitar(name="ESP F-104",
                   description="The ESP F-104 bass not only looks nasty, its 35-inch scale and ESP-designed SB-4 pickups with active EQ lend themselves especially well to crushing, de-tuned sounds. Tune to D or C with heavy strings or string up B-E-A-D for brutal low end. Has a wildly sculpted agathis body, bolt-on maple neck, rosewood fingerboard, dot fretboard inlays with the model name at 12th fret, 24 extra-jumbo frets, and chrome hardware.",
                   slug="esp_f104",
                   views=1844,
                   category=gtrcat8)

gtr_bas_3 = Guitar(name="Washburn Taurus T24",
                   description="The Washburn T24 bass is completely pro in every way, crafted using fine tonewoods, advanced construction techniques, and high-quality components. The multi-laminate neck-thru construction features a mahogany body, maple/mahogany neck, rosewood fingerboard with offset dot inlays, custom JJ pickups, and Grover bass tuners.",
                   slug="washburn_t24",
                   views=1045,
                   category=gtrcat8)

gtr_bas_4 = Guitar(name="Yamaha TRBX305",
                   description="The TRBX305's perfectly balanced, ultra-comfortable solid mahogany body with a fast, ultra-comfortable 5-piece maple and mahogany neck and rosewood fingerboard provides the optimum tonal foundation while the Performance EQ active circuitry gives instant access to perfectly dialed-in stage-ready tones coupled with the expressive control you need.",
                   slug="yamaha_trbx305",
                   views=985,
                   category=gtrcat8)

gtr_bas_5 = Guitar(name="Ibanez SR400QM",
                   description="With its thin five-piece SR4 maple/rosewood neck, the Ibanez SR400QM electric bass stands proudly in the wide line up of the SR family. The lightweight, balanced comfort-contoured mahogany body helps make playing easy and comfortable, while the CAP EXF-N2 pickups provide well-balanced tone from each string. The gorgeous quilted maple top adds a killer look to a bass that does it all.",
                   slug="ibanez_sr400qm",
                   views=996,
                   category=gtrcat8)

gtr_bas_6 = Guitar(name="Epiphone Thunderbird-IV",
                   description="The Thunderbird IV was one of the most radical designs to come out of the Gibson and Epiphone Kalamazoo factory in the early 60s, thanks to legendary automotive designer Ray Dietrich, who was asked to put a new twist on solidbody guitars and basses. The sound of the Thunderbird IV was as cutting edge as its design and now the Thunderbird Classic-IV PRO returns with all of Epiphone's first-class quality and a lifetime guarantee, but without the hassles of owning (or hiding) a vintage instrument.",
                   slug="epiphone_thunderbird",
                   views=805,
                   category=gtrcat8)

gtr_bas_7 = Guitar(name="Squier Jaguar Bass V",
                   description="Squier's most versatile Jaguar bass model is even more versatile now, with the extended range of the Vintage Modified Jaguar Bass V Special five-string model. You get all the sharp looks, fantastic tone and great features of its four-string brother, now with the addition of an earth-shaking low B string.",
                   slug="squier_jaguarv",
                   views=664,
                   category=gtrcat8)

gtr_bas_8 = Guitar(name="Epiphone EB-3",
                   description="The EB-3 Bass quickly became one of the most attractive and distinctive basses in rock and players like Bill Wyman of The Rolling Stones, Cream's Jack Bruce, and The Who's John Entwistle made rock history on SG-style basses. This latest iteration of a legendary mainstay is a stunning recreation of the vintage marvel with all the tone and feel of the original without the vintage price tag and vintage problems.",
                   slug="epiphone_eb3",
                   views=2041,
                   category=gtrcat8)

gtr_bas_9 = Guitar(name="Rogue LX200BF",
                   description="The LX200BF fretless bass guitar features an extended maple neck, rosewood fingerboard, covered traditional-style split and single-coil pickups, 2 volume and 2 tone controls, die-cast machine heads, and black hardware. Rogue priced the 4-string LX200BF bass to make it easy to add a fretless to your arsenal.",
                   slug="rogue_lx200bf",
                   views=1225,
                   category=gtrcat8)

session.add(gtr_bas_1)
session.add(gtr_bas_2)
session.add(gtr_bas_3)
session.add(gtr_bas_4)
session.add(gtr_bas_5)
session.add(gtr_bas_6)
session.add(gtr_bas_7)
session.add(gtr_bas_8)
session.add(gtr_bas_9)
session.commit()


# Add Double-Neck Guitars
gtr_dbl_1 = Guitar(name="Epiphone LE G-1275 Custom",
                   description="The G-1275 is based on the vintage original 1235 Doubleneck that was first produced at the legendary Gibson/Epiphone Kalamazoo, Michigan factory in 1963. It quickly became one of the most sought-after and original guitars in rock. The 6-string and 12-string each have their own Epiphone all-metal 3-way toggle switch to select each guitar's pickups. There is also a second master all-metal 3-way toggle switch located between the 6-string and 12-string bridge.",
                   slug="epiphone_g1275",
                   views=36,
                   category=gtrcat9)

gtr_dbl_2 = Guitar(name="Ovation CSE225-RRB",
                   description="With its specially designed Super-Shallow composite body-a favorite of stage performers-Ovation's Celebrity double neck combines 6- and 12-string guitars into a single, easy-to-play instrument. With a figured maple top and matched, lightweight bracing that's designed to enhance punch and projection, this guitar covers all the bases. Ovation's pioneering multi-sound hole design enhances string vibration and sustain by improving soundboard efficiency. Both slim necks are easy to play, and twin cutaways insure easy access to the either fret board.",
                   slug="ovation_cse225rrb",
                   views=102,
                   category=gtrcat9)

gtr_dbl_3 = Guitar(name="Dean Gran Sport DBL WBS",
                   description="This guitar sports a more traditional form that's easily recognizable with its double-cutaway mahogany body and set mahogany C-shape necks. The rosewood fingerboards have pearl GS inlays and single-ply neck bindings. Chrome hardware includes Grover tuners and Tune-O-Matic bridges. Sound is what counts and the GS DBL is equipped with DMT Series pickups wired to a 3-way switch and dual master Volume and Tone controls.",
                   slug="dean_gsdblwbs",
                   views=87,
                   category=gtrcat9)

gtr_dbl_4 = Guitar(name="Zenison Double-Neck Electric",
                   description="The Zenison double-neck guitar features custom-painted neck and headstock, pearloid white pickguard, and 22-fret necks with a fixed bridge on the 12-string neck and a vintage-style tremolo on the six-string neck. Unique, affordable option for anyone looking for that double-neck look, feel, and sound without having to break the bank.",
                   slug="zenison_dblneck",
                   views=75,
                   category=gtrcat9)

session.add(gtr_dbl_1)
session.add(gtr_dbl_2)
session.add(gtr_dbl_3)
session.add(gtr_dbl_4)
session.commit()

print "    All items were added successfully!"

session.close()

print "==> Database connection terminated; exiting application...\n\n"
