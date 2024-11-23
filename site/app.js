function showForm(type) {
    document.querySelectorAll('.btn-type').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.form-content').forEach(content => content.classList.add('hidden'));
    
    document.getElementById(type).classList.remove('hidden');
    document.querySelector(`[onclick="showForm('${type}')"]`).classList.add('active');
}

const cars = [
    {
        title: "اجاره جنسیس کوپه",
        model: "مدل 2016",
        dailyPrice: "8,500,000",
        monthlyPrice: "80,000,000",
        imgSrc: "images/Frame 427320662.png"
    },
    {
        title: "اجاره تویوتا لندکروزر در تهران 2013",
        model: "مدل 2013",
        dailyPrice: "8,500,000",
        monthlyPrice: "80,000,000",
        imgSrc: "images/Frame 427320662 (1).png"
    },
    {
        title: "اجاره بنز E250 سدان",
        model: "مدل 2016",
        dailyPrice: "8,500,000",
        monthlyPrice: "80,000,000",
        imgSrc: "images/Frame 427320662 (2).png"
    },
    {
        title: "اجاره بنز کروک",
        model: "مدل 2016",
        dailyPrice: "8,500,000",
        monthlyPrice: "80,000,000",
        imgSrc: "images/Frame 427320662 (3).png"
    },
    {
        title: "اجاره هیوندای توسان 2014",
        model: "مدل 2014",
        dailyPrice: "8,500,000",
        monthlyPrice: "80,000,000",
        imgSrc: "images/Frame 427320662 (4).png"
    },
    {
        title: "اجاره بی ام و 528",
        model: "مدل 2016",
        dailyPrice: "8,500,000",
        monthlyPrice: "80,000,000",
        imgSrc: "images/Frame 427320662 (5).png"
    }
];

// ایجاد کارت‌ها به صورت داینامیک
function createCarCards() {
    const carList = document.getElementById("car-list");
    
    cars.forEach(car => {
        const carCard = document.createElement("div");
        carCard.classList.add("col-12", "col-sm-6", "col-md-4", "mb-4");
        
        carCard.innerHTML = `
            <div class="car-card">
                <div class="position-relative">
                    ${car.discount ? `<span class="discount-badge">${car.discount}</span>` : ''}
                    <img src="${car.imgSrc}" alt="${car.title}">
                </div>
                <div class="p-3">
                    <h6>${car.title}</h6>
                    <p class="text-muted">${car.model}</p>
                    <div class="price-row">
                        <span>روزانه</span>
                        <span class="price-value">${car.dailyPrice} تومان</span>
                    </div>
                    <div class="price-row">
                        <span>ماهانه</span>
                        <span class="price-value">${car.monthlyPrice} تومان</span>
                    </div>
                    <div class="price-row mt-2">
                        <span>مبلغ ضمانت:</span>
                        <span class="text-muted">80 میلیون تومان</span>
                    </div>
                </div>
                <button class="btn reserve-button">درخواست رزرو</button>
            </div>
        `;

        carList.appendChild(carCard);
    });
}


// اجرای تابع ایجاد کارت‌ها هنگام بارگذاری صفحه
createCarCards();

