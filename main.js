const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    backgroundColor: '#1d1d1d',
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

const game = new Phaser.Game(config);

function preload() {
    // بارگذاری تصویر پس‌زمینه و گرید
    this.load.image('background', 'assets/images/background.png');
    this.load.image('grid', 'assets/images/grid.png'); // گرید زمین
    // بارگذاری تصویر کاراکتر
    this.load.image('player', 'assets/images/player.png');
}

function create() {
    // اضافه کردن پس‌زمینه
    this.add.image(400, 300, 'background').setOrigin(0.5, 0.5);

    // اضافه کردن گرید به عنوان زمین
    this.add.image(400, 300, 'grid').setOrigin(0.5, 0.5);

    // اضافه کردن کاراکتر به زمین
    this.player = this.add.sprite(100, 300, 'player').setScale(0.5); // کوچک کردن سایز کاراکتر
    this.player.setInteractive(); // قابل کلیک کردن

    // متغیر برای ردیابی کاراکتر انتخاب شده
    this.selectedPlayer = null;

    // اضافه کردن کلیک روی کاراکتر
    this.player.on('pointerdown', () => {
        this.selectedPlayer = this.player; // انتخاب این کاراکتر
        console.log('Player selected!');
    });

    // اضافه کردن کلیک روی زمین برای قرار دادن کاراکتر
    this.input.on('pointerdown', (pointer) => {
        if (this.selectedPlayer) {
            this.selectedPlayer.x = pointer.x; // انتقال کاراکتر به موقعیت کلیک
            this.selectedPlayer.y = pointer.y;

            console.log(`Player moved to: (${pointer.x}, ${pointer.y})`);
        }
    });

    // تنظیم کلید برای تغییر جهت
    this.input.keyboard.on('keydown-R', () => {
        if (this.selectedPlayer) {
            const flipped = this.selectedPlayer.flipX;
            this.selectedPlayer.setFlipX(!flipped); // جهت رو برعکس می‌کنه
            console.log('Player direction changed!');
        }
    });
}

function update() {
    // فعلاً نیازی به آپدیت لحظه‌ای نیست
}