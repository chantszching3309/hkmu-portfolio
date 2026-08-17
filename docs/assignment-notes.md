# Assignment notes

只收錄自己寫嘅答案。官方題目、老師評語、論文原文句子冇放。

作者：Chan Tsz Ching

---

## ITS2340 Web design（文字部分）

網頁 code 喺 `web/` 同 `completed/web/`。

### TMA1

Chan Tsz Ching

Q1
a)
<a href="http://www.recipes.com" target="_blank" >
Click here for recipes </a>

b)
(see web/tma1.html)

Q2
a)
The <title> element defines the title of the document. It won't display in document content.
<title>Hong Kong Monetary Authority</title>

b)
<meta charset="utf-8">
It is made for displaying characters correctly and ensures consistent rendering of text across different web browsers, operating systems, and devices and avoids garbled.

c)
It can improve users to click on your link.

d)
It isn't because meta keywords have been ill used in the past, add unrelated keywords to control search ranking.

e)
<meta property="og:url" content="//www.hkma.gov.hk/eng/">
<meta property="og:image" content="https://www.hkma.gov.hk/media/eng/img/share.jpg?v=1">
Increasing your content's visibility, and content optimization.

f)
<script src="/statics/assets/js/p.js"></script>
<link href="/statics/assets/css/custom-ui.css?v1" rel="stylesheet" type="text/css">
<link href="/statics/assets/css/print-ui.css" rel="stylesheet" type="text/css" media="print">

g)
<meta name="viewport" content="width=device-width, minimal-ui, initial-scale=1, maximum-scale=1, minimum-scale=1">
It defines a webpage’s settings and controls the settings of content on different devices.

Q3
a)
First, desktop file size is more than mobile file size. Then, we look for loading time, because loading speed of mobile 4g is slower than desktop chrome, so mobile needs more time for loading versus desktop. Interaction to Next Paint (INP): mobile is better. Desktop is faster than mobile on First Contentful Paint (FCP) and Time to First Byte (TTFB). Desktop is effective on Cumulative Layout Shift (CLS) and Largest Contentful Paint (LCP), but mobile is worse on them. But, mobile is better than desktop on Interaction to Next Paint (INP).

b)
IT S234 Web design evaluation checklist
Website URL: https://www.hktvmall.com/hktv/en/
Date: 8 Nov
Assign a score between 1 and 10 for each category, with 10 being the highest.

Criteria | Score (1 to 10)
Speed — homepage downloads quickly | 10
It's so fast when you tap on it and it opens in just a few seconds.
First impression — general appearance | 10
The homepage is attractive, has strong eye appeal by many high quality photos and words with colour. Every page is so clearly that shows the product where it is, all is clearly expressed.
Visual appeal | 10
The look and feel of the site are appropriate and complementary to its content.
Ease of navigation | 10
You can tell where you are within the site at all times on the name of the tab.
Use of graphics/sound/video | 10
The graphics are clearly labelled, clearly identified every product.
Content/Information | 10
The site has been recently created/revised.
Usability | 10
You imagine that most people would learn to use this web site very quickly.
Total Score (out of 70): 70

Q4
a)
Quick loading time: It has a quick loading time to ensure users remain engaged.
Easy access to information: It provides links to important sections such as the Help Center.
Visual quality: The page is visually clean but it lacks eye-catching design, leading to a bland visual of the site.
Unified site design: It provides consistent style and fonts to keep the content unified.
usability: It provides a search box for easy access to information. It also supports browsing through photos, which some people may prefer.

b)
1. Analysis and planning
2. Information and navigation design
3. Interface and graphic design
4. Content production
5. Coding and testing
6. Publishing and promotion
7. Site maintenance

c)
i) The first stage of progress: “analysis and planning”.
ii) Fourth stage of progress: “content production”.
iii) Seventh stage of progress: ”site maintenance”.
iv) Sixth stage of progress: “publishing and promotion”.
v) Fourth stage of progress: “content production”.
vi) Third stage of progress: “interface and graphic design”.
vii) Second stage of progress: “navigation design”.

Q5
a)
It is for describing the presentation of the web, by using colour, fonts, and layout.

b)
(see web/q5b-welcome.html)

c)
<link href="styles.css" rel="stylesheet"/>

d)
It is not reusable, such as if multiple elements need the same style then the CSS code must be copied for each element.
Poor readability of code, it mixes CSS with HTML makes code harder to read.

e)
<section> can include many <article> tags, it is supposed to be discussed around a central theme. It used for grouping content.
<article> tag specifies independent, self-contained content, such as a blog post, news story.

f)
Using group selector on multiple elements with the same pattern in the same line to show where the style is. e.g. selector=h1,h2

h1,h2{
colour:blue;
font-size:300px
}

The descendant selector displays the same pattern on target elements by parent element, and no need to write in the same line.
e.g. div p {background-color: blue;}

g)
#header {
background-color: lightblue;
padding: 10px; }

h)
button:hover{
border:3px solid red;}

i)
a:link {
font-style: italic ; }

j)
(see practice/web/q5j-css-examples.html)

k)
<p style=" text-align:center ;"> </p>

Q6
URL: ucourse.hkmu.edu.hk/~s1381772

### TMA2

Chan Tsz Ching



Q1
a)
Reinforce brand identity: Graphics make sites more beautiful and professional.
Show navigation: It makes the site more user-friendly with graphics that guide users with icons.
Break up text, make it less text-heavy: Use graphics to replace complex information to create more easily understood content.

b)
Bitmap formats: Cannot be freely resized, JPEG
Vector formats: Can be freely resized, SVG

c)
resampling, delete some pixels to decrease the size or estimate the colour to create some new pixels based on the surrounding pixels.

d)
It is a set of colours designed to display consistently on different web browsers.
It ensures consistency on old devices.

e)
Red

f)
RGB mode: p {color: rgb(255, 0, 0);} (255 is 100% )
Hexadecimal code values: P {color: #FF0000;}
(represented by RRGGBB, 00 is the smallest, FF is the largest)

g)
p {color: rgb(255, 0, 0,0.2);}

h)
body{
background-image: url('pics/bg.webp');
background-attachment: fixed;
background-position: top right;
background-repeat: no-repeat
}

Q2
a)
difficult to maintain: It provided complex programming, making it difficult to find mistakes and upgrade. Instead of CSS, CSS has a clear separation of content and styling.
Inflexible: Tables default to a fixed weight and height of display that makes them break on different screen sizes. CSS provides flexible techniques.
Long loading time: Tables usually have more bytes of markup.
Unfriendly to search engines: Tables are designed to display data, not for layout, making it difficult for crawlers to find keywords in complex tables.

b)
URL: http://ucourse.ouhk.edu.hk/~s1381772/tma2/q2b.html
(see web/q2b.html)

Q3
a)
Inline is start on a new line, block and inline-block are allow other elements to their left and right.
Block and inline-block can set the width, height, margin top and bottom, but inline cannot.
All can respects margin-left and margin-right.

b)
URL: http://ucourse.ouhk.edu.hk/~s1381772/tma2/q3b.html
(see web/q3b.html)

c)
URL: http://ucourse.ouhk.edu.hk/~s1381772/tma2/q3c.html
(see web/q3c.html)

Q4
a)
URL: http://ucourse.ouhk.edu.hk/~s1381772/tma2/q4a.html
(see web/q4a.html)

The page uses a flexible container and CSS media queries to rearrange the sections:
- Wide screens (≥781px): The three sections sit in a row, each taking up roughly one-third of the container width.
- Medium screens (480px to 780px): The layout switches to two columns. The first two sections will fill the first row, and the third section will move to the next row, also taking half the width.
- Narrow screens (≤480px): The sections stack vertically, with each one stretching to nearly the full width of the browser.

b)
URL: http://ucourse.ouhk.edu.hk/~s1381772/tma2/q4b.html
(see web/q4b.html)

c)
The viewport means changing the web size depending on the device screen size. width=device-width means set the width of the web equal to the device width, initial-scale=1.0 is the content shows without zooming. “meta” tells the browser how to show the screen, ensure it works normally, device width 1:1 with page width.


### TMA3

1)
a)

b)
<img src="../events/images/winter.jpg" alt="winter image">

c)
Linear: It provides information in a specific order, and it can be read forward or backward. Such as the order meal process.

Hierarchical: It is the most common structure on the web, it provides pages or content as a tree, allowing the user to jump to another page without going back to the home page.

Matrix structure: The content is structured by the user's selection, like select colour, price, and size. Such as a clothing or e-commerce website.

Organic structure: It provides a search bar for typing keywords or tags. The content is related, but it does not have a specific classification. Such as Pinterest.

d)
Where am I?
Show their current location relative to the rest of the site.

Where can I go?
The user can use the drop-down menus to search for items.

How do I get there?
Easy-to-understand links allowed the user to click on.

How do I get back to where I started?
Pressing the home button to return to their starting point.

e)
Sitemaps, drop-down menus, graphics or icons, breadcrumb trails.

2)
a)
method="Get": URL using "?" and adding before the data. Limit URL length. Low security by showing data on a URL. It does not support non-ASCII characters.
method="Post": Use when the form values contain non-ASCII characters or exceed 2048 characters. It is written in the body so it is safer.

b)
<input type="text">
Both do not need to be hidden, so they cannot use "password". They are not an option so do not use a "checkbox" and "radio". "text" is free input.

c)
radio button provides users to select only one option. It has the same attribute in a selection group. Once an option is ticked, any previous selection will automatically be de-selected.
The check box allows the user to select more than one option. It can have different attributes in a selection group.

d)
<input type="radio" name="color" id="blueOption" value="blue">
<input type="radio" name="color" id="redOption" value="red">
"name" is submitted data to the server. The "id" is used to identify an element.
Elements can not have the same id value. "id" matches with "label".

e)
Allow users to use the Tab key to go through all fields in sequential order using tabindex="0". tabindex="-1" for skipping some unnecessary fields. If tabindex=positive index, it would break the natural order.

3)
a)
Enhancing the aesthetic appeal and functionality.
Quality: Ensure that multimedia content fits on different screen sizes without fixed pixels and increase the frame rate.
Media hosting services: For uploading, editing, and hosting multimedia to decrease delay and loading time.
Provide text alternatives: Describe the image and video, or radio by text. Using alt on <img>.
Various user preferences.

b)
HTML is the base structure for defining the relation of content. CSS controls the visual content layout. JavaScript increases interactivity for richness user experience. They improve maintainability, performance, accessibility, and cross-browser reliability.

c)
Internal JavaScript: Written inside HTML <script>, and <script> is in the <head> or before </body>. External JavaScript: using .js.

d)
Browser event such as onclick. Automatic: page load.

4)
URL: http://ucourse.hkmu.edu.hk/~s1381772/TMA3/tma3.html
(see web/tma3.html)


---

## COMP2580 Python（非 code 部分）

程式喺 `python/`。

Q1
e)
i.
(lg N)O = (log 1000 / log 2) *0.001 = 9.97*0.001 = 10*0.001 = 0.01
(N lg N)O = 1000 log 1000 *0.001 = 1000 (10) 0.001 = 10
(N^2)O = 1000^2*0.001 = 1,000,000*0.001 = 1,000
(N^3)O = 1000^3*0.001 = 1000000000*0.001 = 1,000,000

ii.
Algorithm A, because it would not be affected by executing the amount of data.

f)
initialize: Cat Dog Fish And Bee Wolf Bear Lion Tiger Horse
1: Cat vs Dog = Cat , Cat vs Fish = Cat , Cat vs Ant = Ant , Ant vs Bee = Ant , Ant vs Wolf = Ant , Ant vs Bear = Ant , Ant vs Lion = Ant , Ant vs Tiger = Ant , Ant vs Horse = Ant.
=[Ant Dog Fish Cat Bee Wolf Bear Lion Tiger Horse] (9 times)
2: Dog vs Fish = Dog , Dog vs Cat = Cat , Cat vs Bee = Bee , Bee vs Wolf = Bee , Bee vs Bear = Bee , Bee vs Lion = Bee , Bee vs Tiger = Bee , Bee vs Horse = Bee.
=[Ant Bee Fish Cat Dog Wolf Bear Lion Tiger Horse] (8 times)
3: Fish vs Cat = Cat , Cat vs Dog = Cat , Cat vs Wolf = Cat , Cat vs Bear = Cat , Cat vs Lion = Cat , Cat vs Tiger = Cat , Cat vs Horse = Cat.
=[Ant Bee Cat Fish Dog Wolf Bear Lion Tiger Horse] (7 times)
4: Fish vs Dog = Dog , Dog vs Wolf = Dog , Dog vs Bear = Dog , Dog vs Lion = Dog , Dog vs Tiger = Dog , Dog vs Horse = Dog.
=[Ant Bee Cat Dog Fish Wolf Bear Lion Tiger Horse] (6 times)
5: Fish vs Wolf = Fish , Fish vs Bear = Bear , Bear vs Lion = Bear , Bear vs Tiger = Bear , Bear vs Horse = Bear.
=[Ant Bee Cat Dog Bear Wolf Fish Lion Tiger Horse] (5 times)
6: Wolf vs Fish = Fish , Fish vs Lion = Fish , Fish vs Tiger = Fish , Fish vs Horse = Fish.
=[Ant Bee Cat Dog Bear Fish Wolf Lion Tiger Horse] (4 times)
7: Wolf vs Lion = Lion , Lion vs Tiger = Lion , Lion vs Horse = Lion.
=[Ant Bee Cat Dog Bear Fish Lion Wolf Tiger Horse] (3 times)
8: Wolf vs Tiger = Wolf , Wolf vs Horse = Wolf.
=[Ant Bee Cat Dog Bear Fish Lion Wolf Tiger Horse] (2 times)
9: Tiger vs Horse = Horse.
=[Ant Bee Cat Dog Bear Fish Lion Wolf Horse Tiger] (1 time)
Total comparisons = 45 times.

Code files are in python/ and completed/python/.


---

## English short writing（自己嘅文字）

### Reading response

The issue of the passage is about some doctors in hospital are insensitive and they don't interact with patients. Related in HK as well. Because there are too many patients and high change of patients, which makes doctors have to rush to figuring out the problem. For example, I saw a similar situation when my father was in the hospital. The doctor came so fast then he quickly talked about his situation of body health with little eye contact, and talked about his treatment plan in front of his family. It makes the patient and their family feel ignored and worried. Although doctors are under a lot of pressure and have limited time, they should not ignore patients' mental health. Taking a few minutes to be caring and connect with patients can really help them feel better and trust the doctor. In medical care, it is important to balance efficiency and care to improve services in Hong Kong.

### E-learning paragraph（約 190 words）

E-learning is useful, especially in higher education schools, and there are some benefits. First, it is flexible, allowing students to choose when and where to study which makes it easier to fit it into their schedules (Arkorful & Abaidoo, 2015). Second, e-learning improves the power of knowledge and skills, allowing students to gain abundant information without much trouble. Moreover, it provides a chance for learners between them through discussion forums. E-learning can be useful in removing blocks hindered by having trouble getting along with people. Such as some learners are uncomfortable with face-to-face interaction with others. Basically, e-learning simplifies communication and helps the connection that support learning. Fourthly, it is good value for money, which means learners don't need to pay money to go to school. Also, it supports many opportunities for learning without needing many physical spaces. Finally, e-learning depends on the differences of learners. For example, some learners are focused on some topics, while others are ready for review before covering material and exploring deeper. Sum up, e-learning offers flexibility, enhances knowledge, helps communication, and provides many learning opportunities. It gives many learners, making education accessible and efficient without barriers of traditional.

### Paraphrase notes（只寫自己點改，唔抄來源原文）

1. Change wording and structure: I started from "allowing" and used "choose" instead of a longer phrase about having the luxury of choosing.
2. Acknowledge authors' names: I mention (Arkorful & Abaidoo, 2015) after the first point.
3. Use synonym and preserving meaning: I rewrote the idea of reducing social anxiety in my own words, and replaced "cost effective" with "good value for money".

---

## COMP2600 Computer Architecture（自己嘅計算／解釋）

### Assignment 1

Q1
a) Computer is structured by binary number, hexadecimal and octal.
The binary system allows more high efficiency and error-free transmission in data communication.

b) 
More clear and readable for humans. Hex is represented by 0-9 and A to F.

c) 
i) 4x8^3 + 5x8^2 + 6x8^1 + 7x8^0
=2028 + 320 + 48 +7
=2423 oct

ii) oct convert to dec
4x8^2 + 5x8^1 + 6x8^0
=256 + 40 + 6
=302
oct convert to bit
2 | 302 …0
2 | 151 …1
2 | 75 …1
2 | 37 …1
2 | 18 …0
2 | 9 …1
2 | 4 …0
2 | 2 …0
2 | 1 …1

= 100 101 110 binary

iii)
1101 1011 1111
=13     11     15
=D B F

d)
dec convert to binary
= 1011 1111 0110 0001 1100 0
bit convert to hex
0001 0111 1110 1100 0011 1000
=  1      7     14     12     3       8
= 1 7 E C 3 8

e)
1’s complement, use binary of positive integers, and change each 0 to a 1 and each 1 to a 0.
+99 dec = 0110 0011 binary
so -99 = 1001 1100 binary

2’s complement, plus 0001 to negative integers.
-99 dec + 0001 = 1001 1100 + 0001 
= 1001 1101 binary

f)
range=[-2^(n-1) , 2^(n-1)-1]
n=32 , 2^n-1 = 2^31 = –2,147,483,648 
 2^(n-1)-1 = 2^31-1 = 2,147,483,647
range=[ –2,147,483,648 , 2,147,483,647 ]

Q2
i)
Number written in the form “mantissa × 10 ^exponent”.
It can be represented by 12345 x 10 ^0, the mantissa is 12345 and the exponent is 0.
positive: 12.345 x 10 ^3, the mantissa is 12.345 and the exponent is 3.
negative: 12345000 x 10 ^-3, the mantissa is 1234500000 and the exponent is -3.

ii)
JPEG and PNG are used for bitmap but SVG is used for vector.
JPEG
Advantages: Small file size.
Disadvantages: Lossy, removes some data when storing. Not fit for the show detail lines or words.
Smaller files let the internet load quickly in the past.

PNG
Advantages: Lossless, stores all data and supports transparency.
Disadvantages: Larger file sizes than JPEGs. High-quality but not fit for every size.
Using on GIF to provide clear lines to make the images be detailed.

SVG
Advantages: No need for compression, high-quality image in any size.
Disadvantages: Small file sizes, poor support for older browsers.
It can be used on an animation with high-quality on any size.

iii)
Binary-coded decimal, four bits of binary value to represent a decimal digit (0-9).
4-bit =0010 0011 0101 BCD

iv)
Resolution: Vector images remain smooth and sharp at any size, but bitmap images lose quality when the photo is zoomed in.
File size: The vector file size is smaller, as it only stores the mathematical formula.

v)
Double precision has 64 bits is more than 32 bits of single precision, so it has more storage and it provides higher accuracy of storing more decimal places to reduce calculation errors.
The single precision stores numbers with about seven significant digits and values in the approximate range of 10 ^–45 to 10 ^38. The double precision supports about fifteen significant digits and values in the approximate range of 10 ^–324 to 10 ^308.

vi)
Carry flag occurs when result is too large to fit in the result area automatically after adding or subtraction two binary numbers. When 1+1, it equals to 0, and 1 is added to the next addend. When 1+0, it equals to 1.

vii)
i.
40 dec = 0010 1000 binary , 75 dec = 0100 1011 binary
00101000 + 01001011= 01110011 bit
The result of 40+75 is a positive result, and the binary with 8-bit is 0 in frist digit, it represent positive value when 0 is frist digit of bit, so it hasn't underflow or overflow. 

ii.
80 dec = 01010000 bit , 30 dec = 00011110 bit
-30 dec = 11100001 + 00000001 bit = 11100010 bit

80 dec + -30 dec = 01010000 + 11100010 = 100110010 bit
8-bit of ans = 0011 0010
The result of 80-30 = 50 ,50 is a positive, and the binary with 8-bit is 0 in frist digit,it represent positive value when 0 in frist digit of bit, so it hasn't underflow or overflow.

iii.
117 dec = 0111 0101 bit
-117 dec = 1000 1010 + 0000 0001 = 1000 1011 bit

110 dec = 0110 1110 bit 
-110 dec = 1010 0001 + 0000 0001 = 1001 0010 bit

-117 dec + -110 dec
=1000 1011 + 1001 0010
=1 0001 1101 bit
8-bit = 0001 1101
The result of -117-110 is a negative result. The binary with 8-bit is 0 in the first digit,it means the result changes from negative to positive, which is an error, so it is an overflow.

Q3
a)
i)
345 dec = 101011001 bit

0.625 x 2 = 1.25 = 1 bit
0.25 x 2 = 0.5 = 0 bit
0.5 x 2 = 1 bit
result = 101011001.101
ii)
38 dec = 100110 bit
0.99 x 2 = 1.98 = 1 bit
0.98 x 2 = 1.96 = 1 bit
0.96 x 2 = 1.92 = 1 bit
0.92 x 2 = 1.84 = 1 bit
0.84 x 2 = 1.68 = 1 bit
0.68 x 2 = 1.36 = 1 bit
0.36 x 2 = 0.72 = 0 bit
0.72 x 2 = 1.44 = 1 bit

result = 100110.111111(up to 6 decimal point places)

b)
positive integer:
1x2^4 + 1x2^3 +1x2^2 + 0x2^1 + 1x2^0
=16+8+4+0+1
=29
decimal integer:
0x2^-1 = 0
1x2^-2 = 0.25
0x2^-3 = 0
1x2^-4 = 0.0625
0x2^-5 = 0
1x2^-6 = 0.015625

result = 29 + 0.25 + 0.0625 + 0.015625 = 29.328125

ii)
1x2^-1 = 0.5
0x2^-2 = 0
0x2^-3 = 0
1x2^-4 = 0.0625
0x2^-5 = 0
1x2^-6 = 0.015625
0x2^-7 = 0
1x2^-8 = 0.00390625

result = 0.5 + 0.0625 + 0.00390625 = 0.58203125

c)
i)
1012.88 x 1000 
=1.01288 x 10^3

ii)
0.09998 / 100 
=9.998 x 10^-2
d)
2 dec = 10 bit
=1.0 x2^1
single precision exponent + exponent =127 + 1 = 128
128 dec = 1000 0000 bit
2 dec is positive , so sign is 0, and no mantissa.
result = 0 10000000 00000000000000000000000

e)
Simplified comparison, compare the integer to make the CPU execute faster.
Unified range, no need to compute sign logic.

f)
integer:
6120 dec = 1011111101000 bit

decimal:
0.3125 x2 = 0.625 =0
0.625 x2 = 1.25 =1
0.25  x2 = 0.5 =0
0.5 x2 = 1 =1
0.3125 dec = 0.0101 bit

-6120.3125 dec = -(1011111101000.0101) bit
= -(1.0111111010000101)x 2^13

exponent = 13 + 127 = 140
140 dec = 10001100 bit
result = 1 10001100 01111110100001010000000

g)
Use the prefix 0x to denote hex numbers.
4992976a =
4 x16^7 + 9 x16^6 + 9 x16^5 + 2 x16^4 + 9 x16^3 + 7 x16^2 + 6 x16^1 + 10 x16^0
= 1234343786 dec

Q4
a)
Opcode has 4 bits (0-3), so there are 2^4 = 16 instructions that can be defined. There are 4 bits (4-7), so addressing space has 2^4 = 16 bytes.

b)
This instruction set design is not sufficient. First, it doesn't have an Instruction location counter for keeping track of which instruction is executed next. Second, it doesn't have input/output operations for receiving from and sending to the outside, such as mailboxes, in-basket and out-basket. Also, it needs the exception and break operations to manage error cases. And provide a high-level language for Memory operations.

c)
1. The memory storage space is limited, it only has 100 mailboxes, starting from 00 to 99 with 3 digits in each mailbox.
2. Lack of complex functions on calculator, it only supports integer addition and subtraction.
3. Single-string design: it only executes one instruction at a time, multitasking systems are common today.

d)
Because assembly codes are human-friendly, they are short and easy to remember names. Thus, it is readable and easy to use. And it uses the Instruction location counter to execute instructions that can keep checking which instructions are executed next. Low-level programming uses 0’s and 1’s, and it needs programmers to manually manage memory on receiving and sending.

e)
Because it is only valid for comparing computers with common buses of the same size. 

f)
RTL provides a clear way to describe operations and data flow. It can be executed in parallel.
RTL specifies the execution of instructions in a procedural (step-by-step) manner, each RTL step completes within one clock cycle, allowing programmers to predict execution time.


g)
00 IN
01 STO 99
02 IN
03 ADD 99
04 OUT
05 HLT

h)
91 → MAR
M[MAR] → MDR
MDR → ACC

92 → MAR
M[MAR] → MDR
ACC + MDR → ACC

93 → MAR
ACC → MDR
MDR → M[MAR]
HLT

### Assignment 2

Q1

a)
It serves as a bridge between CPU and I/O interface, providing effective data transfer between core components and I/O peripherals.

b)
i.
800 x 50000 x 6 x 512 = 122 880 000 000 B = 117187.5 MB

ii.
rate per sec: 10000/60 = 166.67 rps
800 x 512 x 10000/60 = 409600 bytes x 166.67 rps
=68268032 bps

iii.
minimum: 0s
maximum:
put y = seconds of one lap
10000 * y = 60 s 
y = 60/10000 = 0.006 s = 6ms 
average: 6ms /2 = 3ms

c) It occurs when the program getting error, such as an interrupt when being executed. It would stop the program, then send the memory address and the next instructions to the PC ,and other related program data to the stack, then execute the instructions in the ISR  to service the interrupt.

d)
non-maskable interrupt
non-maskable interrupt
maskable interrupt

e)
i. 1920/1080 = 16:9
ii. square root of (1920^2 + 1080^2) ~= 2202.9, then 2202.9/14 = 157.35 =157 dpi
iii. 
put x = one pixel
(16x)^2 + (9x)^2 = 14^2
x^2 = 196/337 
x = 0.762628595 =0.763 inch
high = 9(0.762628595) = 6.863 inch, weigh = 16(0.762628595) = 12.202 inch
size of an individual pixel:
12.202/1920 = 0.00635520833 inch
1 inch = 25.4 mm
25.4 x 0.00635520833 = 0.161544 = 0.161 mm
0.161>0.15, so it would not be sufficient for this display.

f)
Raid provides reliability by writing operations to multiple disks to allow the array to continue operating even if one disk is getting an error. But the data would be lost if the disk is damaged. Also, it can reduce average access time.
Data backup is used to fix the data that is damaged.
They are different.
 
Q2
a) Operating system is an intermediary between users and application software and hardware.
Process management: It allocates resources to handle process synchronization, communication, and deadlock handling.
User interface: It is for launching programs. It provides applications with a set of standard user interface components to present information. also It captures user inputs and dispatches them to the appropriate applications.

b) Multiprogramming allows a few jobs to execute at the same time, increasing CPU utilization and reducing resource waste.
Time-sharing provided the misconception of immediate response to the user by switching jobs quickly with the CPU executing one job every single time.

c) It is flexible, it provides services easy to add, modify and delete to emulate a particular operating environment.
It provides modular design, client and server processes are user processes separates services from kernel functions, their failures will not affect the whole system.

d) Embedded systems execute only pre-built software to perform specific tasks. Personal computer provides a widely used user interface by applications.
Regular embedded systems have limited memory, storage space, and processing power to satisfy the specific applications. Personal computer have high-end processors, large amounts of RAM, and extensive storage.

e)
i. ls -lRSh
ii. chmod a+rw file.txt
iii. mv *~
iv. rm -i *.zip
v. grep -i mail  /etc/services
vi. ls /usr/bin | sort -f >> filelist.txt
vii. 
chown mary file /home/mary/memo.txt
chown HKMU file /home/mary/memo.txt

Q3
18
a)
i. Incorrect, program in execution called process, not thread.Thread means a sigle execution in process. A proces can contain more than one threads.
ii. Correct, thread is lightweight process, it has no complex resources comparing with process.
iii. Correct, treads share the data, code and resources of a process, and are more
efficient.
iv. Incorrect, threads share the same address space, global variables and resources.

b)
client/server systems: It switches among peer threads is very efficient, it shares the data, code and resources of a process, and is more efficient, but no protection between threads.
kernel: It supports multi-threading in processes, including Windows.

c) Minimizing turnaround time, minimizing response time, minimizing waiting time, ensuring fairness.

d)
SJF executes the shortest job first before a long job.HRRN Balancing fairness and efficiency can prevent indefinite postponement.

e)
Wait and signal, they are indivisible and cannot be interrupted in the middle. Mutexes ensure there is only one process executing at a time. implemented in hardware, others in software. Avoid confusing the resource count and synchronization fail.

f) It counts the number of occupied spaces in the buffer.
It tells producers the buffer is full to stop input data, and also to ensure consumers execute when the data is not empty.
It starts from 0, then the buffer value adds 1 when the producer inputs data every single time, and minus 1 when consumer takes out the data from buffer every single time.
when “full”=0 , consumer will wait until producer inputs data.

g)
If readers keep making requests, the writers will starve because they can't update the data.

h)
It occurs when a process accesses resources that are indefinitely unavailable due to unfair allocation. Does not necessarily happen.

Q4
a) New, ready, running, blocked, terminated.  Changing state from new to ready is called admission. The state of Ready to the state of running is called dispatch, reverse transition is called timeout. A running process enters the blocked state when its execution cannot proceed and then the process runs to the ready state from the blocked state called wake-up. Finally, it “exit” to the terminated from running state.

b)
CPU executes one job and starts executing another. Saving the state of the old process and loading the state of the new one. It increases response times.

c) 
low-level scheduler. The high-level scheduler executes when admission and exit, but low-level scheduler manages the switching process hundreds of times per second. 

d)
i. (0+12-4+18-10)/3 = 5.33 s
ii. (0+12-10+14-4)/3 = 4 s
iii. (0+4-4+10-10+12-4)/3= 8/3 = 2.67 s
iv. (0+0+6-4+9-6+12-9+15-10+18-12)/3 = 19/3 = 6.33 s

e) 
SJF is non-preemptive, it compares the jobs and orders them from shortest to longest. It will be completed before next job. 
SRT is preemptive, it compares the remaining time, if a new process comes that is shorter than the process being executed, the new process would replace the current process. 

f)
Share data, concurrent process and uncertainty results.

### Assignment 3

Q1
a) It merges the address spaces of different object modules to produce a single absolute load module.

b)
i.secment 2 : phycial address =  2000 + 400  = 2400 
check: offset<limit , 400 < 2134 = correct.

ii.secment 0 : phycial address =  120 + 0  = 120 
check: offset<limit , 0 < 300 = correct.

iii. segment 4 : check: offset<limit, 320 < 245 = incorrect, offset cannot be larger than or equal to limit, error condition.

iv. segment 3 : check: offset<limit, 80 < 80 = incorrect, offset cannot equal limit, error condition.

c) Minimize disk space waste by using internal / external fragmentation. Pervets performance decreases speed.

d) Page fault occurs when accessed page is not in physical memory. The page is only stored in swap space. 
Servicing the fault interrupt routine. Allocating a frame in physical memory for the page, using a free frame. If all frames are occupied, then select one frame page to swap out for a free frame for the requested page. Copy the request page from the swap space to the frame. Update the page table of the process. Restart the process, which then proceeds using the page.

e)
i.

In time 1, page access 6 in Frame A, a page fault occurs.(>6, , , )
In time 2, page access 5 in Frame B, a page fault occurs. (6,>5, , )
In time 3, page access 4 in Frame C, a page fault occurs. (6,5,>4 , )
In time 4, page access 3 in Frame D, a page fault occurs.(6,5,4,>3 )
In time 5, page access 3 in Frame D, no page fault occurs. (6,5, 4, 3 )
In time 6, page access 2 in Frame A, a page fault occurs. (6,5, 4, 3 ) => (>2,5, 4, 3 )
In time 7, page access 1 in Frame B, a page fault occurs. (2,5, 4, 3 ) => (2,>1, 4, 3 )
In time 8, page access 5 in Frame C, a page fault occurs. (2,1, 4, 3 ) => (2,1, >5, 3 )
In time 9, page access 6 in Frame D, a page fault occurs. (2,1, 5, 3 ) => (2,1, 5, >6 )
In time 10, page access 2 in Frame A,no page fault occurs. (2,1, 5, 6 )
In time 11, page access 5 in Frame C, no page fault occurs. (2,1, 5, 6 )
In time 12, page access 2 in Frame A, no page fault occurs. (2,1, 5, 6 )
In time 13, page access 2 in Frame A, no page fault occurs. (2,1, 5, 6 )
In time 14, page access 3 in Frame A, a page fault occurs. (2,1, 5, 6 ) => (>3,1, 5, 6 )

page fault = 9 times

ii.
In time 1, page access 6 in Frame A, a page fault occurs.(>6, , , )
In time 2, page access 5 in Frame B, a page fault occurs. (6,>5, , )
In time 3, page access 4 in Frame C, a page fault occurs. (6,5,>4 , )
In time 4, page access 3 in Frame D, a page fault occurs.(6,5,4,>3 )
In time 5, page access 3 in Frame D, no page fault occurs. (6,5, 4, 3 )
In time 6, the lease used is 6 in Frame A, so swap space. (6,5, 4, 3 ) =>  (>2,5, 4, 3 )
In time 7, the lease used is 5 in Frame B, so swap space. (2,5, 4, 3 ) =>  (2,>1, 4, 3 )
In time 8, the lease used is 4 in Frame C, so swap space. (2,1 4, 3 ) =>  (2,1, >5, 3 )
In time 9, the lease used is 3 in Frame D, so swap space. (2, 1, 5, 3 ) =>  (2, 1, 5, >6 )
In time 10, page 2 is in frame A. (2, 1, 5, 6 )
In time 11, page 5 is in frame C. (2, 1, 5, 6 )
In time 12, page 2 is in frame A. (2, 1, 5, 6 )
In time 13, page 2 is in frame A. (2, 1, 5, 6 )
In time 14, the lease used is 1 in Frame B, so swap space.  (2, 1, 5, 6 ) =>  (2,>3, 5, 6 )

page fault = 9 times

iii.

In time 1, page access 6 in Frame A, a page fault occurs.(>6, , , )
In time 2, page access 5 in Frame B, a page fault occurs. (6,>5, , )
In time 3, page access 4 in Frame C, a page fault occurs. (6,5,>4 , )
In time 4, page access 3 in Frame D, a page fault occurs.(6,5,4,>3 )
In time 5, page access 3 in Frame D, no page fault occurs. (6,5, 4, 3 )
In time 6, it will not be used for the longest time in future is 4 in Frame C, so swap space. (6,5, 4, 3 ) =>  (6,5, >2, 3 )
In time 7, it will not be used for the longest time in future is 3 in Frame D, so swap space.
(6,5, 2, 3 ) => (6,5, 2, 1 )
In time 8, page 5 is in frame B.(6,5, 2, 1 )
In time 9, page 6 is in frame A.(6,5, 2, 1 )
In time 10, page 2 is in frame C.(6,5, 2, 1 )
In time 11, page 5 is in frame B.(6,5, 2, 1 )
In time 12, page 2 is in frame C.(6,5, 2, 1 )
In time 13, page 2 is in frame C.(6,5, 2, 1 )
In time 14, all pages will not be used for the longest time in future, so swap space with FIFO.
(6,5, 2, 1 ) => (>3,5, 2, 1 )

page fault = 7 times

f) OPT is the best, because its page fault occurs only seven times, FIFO and LRU occur 9 times. It selects the page that will not be used for the longest time in future to reduce the time page faults occur in the whole process.

Q2
a)
i.
Advantages:
1. Avoid producing many fragments,the rest of space is large.
2. Reduce the dispersed fragments wasted. They are separate in different spaces and can not be combined for use.
Disadvantages:
1. Wastes a large space on a small memory that can be allocated in a small space.
2. Large memory execution delay: Large space is used, and there have not enough space to get into, the large memory needs to wait for the free space.

ii.
i) Best fit:
P (13KB) get into block 2(16KB), the memory block lefts 18KB,3KB,32KB,28KB.
Q (20KB) get into block 4(28KB), the memory block lefts 18KB,3KB,32KB,8KB.
R (10 KB) will get into block 1 (18KB).The memory block lefts 8KB,3KB,32KB,8KB.

ii) Worst fit:
P (13KB) get into block 3(32KB), the memory block lefts 18KB,16KB,19KB,28KB.
Q (20KB) get into block 4(28KB), the memory block lefts 18KB,16KB,19KB,8KB.
R (10 KB) will get into block 3 (19KB).The memory block lefts 18KB,16KB,9KB,28KB.

iii) First fit: 
P (13KB) get into block 1(18KB), the memory block lefts 5KB, 16KB, 32KB, 28KB.
Q (20KB) get into block 3(32KB), the memory block lefts 5KB, 16KB, 12KB, 28KB.
R (10 KB) will get into block 2 (16KB).The memory block lefts 5KB, 6KB, 12KB, 28KB.

b)
i. page bits = 32 = 2^5, 5 bits for pages. 4096 words = 2^12, 12 bits for words.Logical address bits = 12+5 = 17 bits.

ii. Frame bits = 256 = 2^8, 8 bits for frames.4096 words are the same as a page size = 12 bits. Physical address bits = 12+8 = 20 bits.

c) It is shareable, processes share the same physical address, Variable size to no internal fragmentation, and grows dynamically in memory. Independent segment. Only readable.

d) It occurs when a system spends time on paging more than executing. The performance cannot be loaded into the memory because of a lack of RAM. Then, it would keep swapping pages more than executing the process.

e)
i. CPU stays free usually for waiting pages to get into the disk. Disk keeps busy swapping pages.
ii. Installing more main memory and decreasing the degree of multiprogramming.

Q3
a) Provide logical grouping of files and help to resolve naming, housekeeping, and
file security problems. 

b) user services are the interface and functions visible and accessible to a human, such as creating and deleting, copying, renaming, and displaying files.
Program services are operations concerned with the processing of files by software programs, such as open, read, write file.

c)
linked: It allows an extension file after creation. It does not require index blocks, it avoids waste space for allocating the index blocks, and it has no external fragmentation.

d)
contiguous: because it needs to be side by side to allocate files, not the same as others, it can not be separated to allocate in different spaces. 

e)
Indexed supports better random access than linked, because linked must traverse the list sequentially. Indexed access to any blocks by looking up their addresses in the index block.
Linked would break the entire chain. Indexed only affects the pointer to the related block.
Indexed is High overhead, even a few pointers also require an entire index block, resulting in large wastage by many small files. linked allocates pointers to FAT.
The first level has a single block pointers to the index blocks in the second level, then the second-level index blocks point to the actual data storage blocks.

f) The user issuing the I/O request is blocked until the I/O operation is completed. 
g)
i. block size = 2^9 , 2^34/2^9 = 2^25 = 33,554,432 blocks
ii. 25 bits
iii. 2^25 x 25 = 838860800 bits = 100MB

h) The user issuing the I/O request is blocked until the I/O operation is completed. 
 
Q4
a)
i. From 22 to 32 = 10( distance )
From 32 to 10 = 22( distance )
From 10 to 8 = 2( distance )
From 8 to 54 = 46( distance )
From 54 to 86 = 32( distance )
From 86 to 24 = 62( distance )
head movement =  174

ii. From 22 to 24 = 2( distance )
From 24 to 32 = 8( distance )
From 32 to 10 = 22( distance )
From 10 to 8 = 2( distance )
From 8 to 54 = 46( distance )
From 54 to 86 = 32( distance )
head movement =  112

iii. 22 -> 24 = 2
24 -> 32 = 8
32 -> 54 = 22
54 -> 86 = 32
86 -> 100 = 14
100 -> 10 = 90
10 -> 8 = 2
head movement =  170

iv. 22 -> 24 = 2
24 -> 32 = 8
32 -> 54 = 22
54 -> 86 = 32
86 -> 10 = 76
10 -> 8 = 2
head movement =  142

v. 22 -> 24 = 2
24 -> 32 = 8
32 -> 54 = 22
54 -> 86 = 32
86 -> 100 = 14
100 -> 0 = 100
0 -> 10 = 10
10 -> 8 = 2
head movement =  190

vi. 22 -> 24 = 2
24 -> 32 = 8
32 -> 54 = 22
54 -> 86 = 32
86 -> 8 = 78
8 -> 10 = 2
head movement =  144

b) SSTF. LOOK serves the nearest request in the current direction.if there is none, it continues with the nearest request in the opposite direction does not reach the ends needlessly.

c) C-SCAN, it goes back immediately to its starting point. Serving requests along the way in one direction only.

d) SSTF, it choose the requirement with the smallest distance, average distance is shorter. C-LOOK is fixed direction for requirement and back to lowerset requirement.FCFS services requests in arrival order.
