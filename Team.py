import pygame as p
import time
from pygame import mixer

class Cat(p.sprite.Sprite):  # Định nghĩa một lớp mới có tên là Cat, là một lớp con của pygame.sprite.Sprite.

    def __init__(self):  # Đây là hàm khởi tạo cho lớp Cat.
        super().__init__()  # Gọi hàm khởi tạo của lớp cha Sprite.
        self.x = 50  # Tọa độ x của con mèo.
        self.y = HEIGHT / 2  # Tọa độ y của con mèo.
        self.vel = 6  # Vận tốc di chuyển của con mèo.
        self.width = 100  # Chiều rộng của con mèo.
        self.height = 50  # Chiều cao của con mèo.

        # HÌNH ẢNH

        self.cat1 = p.image.load('shipper 1.png')  # Tải hình ảnh 'shipper 1.png' và gán cho self.cat1.
        self.cat2 = p.image.load('shipper 2.png')  # Tải hình ảnh 'shipper 2.png' và gán cho self.cat2.
        self.cat1 = p.transform.scale(self.cat1, (100,100))  # Thay đổi kích thước hình ảnh self.cat1 thành 150x150.
        self.cat2 = p.transform.scale(self.cat2, (100,100))  # Thay đổi kích thước hình ảnh self.cat2 thành 150x150.

        self.image = self.cat1  # Gán hình ảnh hiện tại của con mèo là self.cat1.
        self.rect = self.image.get_rect()  # Lấy đối tượng Rect từ hình ảnh hiện tại của con mèo.
        self.mask = p.mask.from_surface(self.image)  # Tạo một đối tượng Mask từ hình ảnh hiện tại của con mèo.

    def update(self):  # Hàm cập nhật trạng thái của con mèo.
        self.movement()  # Gọi hàm di chuyển.
        self.correction()  # Gọi hàm điều chỉnh.
        self.checkCollision()  # Gọi hàm kiểm tra va chạm.
        self.rect.center = (self.x, self.y)  # Cập nhật tọa độ trung tâm của đối tượng Rect.

    def movement(self):  # Hàm di chuyển con mèo.
        keys = p.key.get_pressed()  # Lấy trạng thái của tất cả các phím.
        if keys[p.K_LEFT]:  # Nếu phím mũi tên trái được nhấn...
            self.x -= self.vel  # Di chuyển con mèo sang trái.
            self.image = self.cat2  # Thay đổi hình ảnh của con mèo.

        elif keys[p.K_RIGHT]:  # Nếu phím mũi tên phải được nhấn...
            self.x += self.vel  # Di chuyển con mèo sang phải.
            self.image = self.cat1  # Thay đổi hình ảnh của con mèo.

        if keys[p.K_UP]:  # Nếu phím mũi tên lên được nhấn...
            self.y -= self.vel  # Di chuyển con mèo lên trên.

        elif keys[p.K_DOWN]:  # Nếu phím mũi tên xuống được nhấn...
            self.y += self.vel  # Di chuyển con mèo xuống dưới.

    def correction(self):  # Hàm điều chỉnh vị trí của con mèo.
        if self.x - self.width / 2 < 0:  # Nếu con mèo đi quá biên trái...
            self.x = self.width / 2  # Đặt lại vị trí của con mèo.

        elif self.x + self.width / 2 > WIDTH:  # Nếu con mèo đi quá biên phải...
            self.x = WIDTH - self.width / 2  # Đặt lại vị trí của con mèo.

        if self.y - self.height / 2 < 0:  # Nếu con mèo đi quá biên trên...
            self.y = self.height / 2  # Đặt lại vị trí của con mèo.

        elif self.y + self.height / 2 > HEIGHT:  # Nếu con mèo đi quá biên dưới...
            self.y = HEIGHT - self.height / 2  # Đặt lại vị trí của con mèo.

    def checkCollision(self):  # Hàm kiểm tra va chạm.
        car_check = p.sprite.spritecollide(self, car_group, False, p.sprite.collide_mask)  # Kiểm tra va chạm giữa con mèo và nhóm xe.
        if car_check:  # Nếu có va chạm...
            explosion.explode(self.x, self.y)  # Gọi hàm nổ.



class Car(p.sprite.Sprite):  # Dòng này định nghĩa một lớp mới có tên 'Car', là một lớp con của 'p.sprite.Sprite'.
    def __init__(self, number):  # Đây là phương thức khởi tạo cho lớp. Nó nhận 'self' và 'number' làm tham số.
        super().__init__()  # Dòng này gọi phương thức khởi tạo của lớp cha 'p.sprite.Sprite'.

        if number == 1:  # Nếu tham số 'number' bằng 1, khối mã sau sẽ được thực thi.
            self.x = 400  # Đặt thuộc tính 'x' của thể hiện 'Car' thành 190.
            self.image = p.image.load(
                'Slow Car.png')  # Tải tệp hình ảnh có tên 'Slow Car.png' và gán nó cho thuộc tính 'image'.
            self.vel = -4  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'Car' thành -4.
        elif number == 2:
            self.x = 580  # Đặt thuộc tính 'x' của thể hiện 'Car' thành 460.
            self.image = p.image.load(
                'Fast Car.png')  # Tải tệp hình ảnh có tên 'Fast Car.png' và gán nó cho thuộc tính 'image'.
            self.vel = 5  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'Car' thành 5.
        elif number == 3:  # Nếu tham số 'number' không phải là 1, khối mã sau sẽ được thực thi.
            self.x = 1050  # Đặt thuộc tính 'x' của thể hiện 'Car' thành 460.
            self.image = p.image.load(
                'Slow Car.png')  # Tải tệp hình ảnh có tên 'Fast Car.png' và gán nó cho thuộc tính 'image'.
            self.vel = 4  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'Car' thành 5.
        else:
            self.x = 1250  # Đặt thuộc tính 'x' của thể hiện 'Car' thành 460.
            self.image = p.image.load(
                'Fast Car.png')  # Tải tệp hình ảnh có tên 'Fast Car.png' và gán nó cho thuộc tính 'image'.
            self.vel = -5  # Đặt thuộc tính 'vel' (vận tốc) của thể hiện 'Car' thành 5.

        self.y = HEIGHT / 2  # Đặt thuộc tính 'y' của thể hiện 'Car' thành một nửa giá trị của 'HEIGHT'.
        self.width = 100  # Đặt thuộc tính 'width' (chiều rộng) của thể hiện 'Car' thành 100.
        self.height = 150  # Đặt thuộc tính 'height' (chiều cao) của thể hiện 'Car' thành 150.
        self.image = p.transform.scale(self.image, (self.width,
                                                    self.height))  # Thay đổi kích thước thuộc tính 'image' để phù hợp với các thuộc tính 'width' và 'height'.
        self.rect = self.image.get_rect()  # Lấy khu vực hình chữ nhật của thuộc tính 'image' và gán nó cho thuộc tính 'rect'.
        self.mask = p.mask.from_surface(
            self.image)  # Tạo một mặt nạ cho thuộc tính 'image' và gán nó cho thuộc tính 'mask'.

    def update(self):  # Hàm cập nhật trạng thái của đối tượng.
        self.movement()  # Gọi hàm di chuyển.
        self.rect.center = (self.x, self.y)  # Cập nhật tọa độ trung tâm của đối tượng Rect.

    def movement(self):  # Hàm di chuyển đối tượng.
        self.y += self.vel  # Tăng tọa độ y của đối tượng theo vận tốc.

        if self.y - self.height / 2 < 0:  # Nếu đối tượng đi quá biên trên...
            self.y = self.height / 2  # Đặt lại vị trí của đối tượng.
            self.vel *= -1  # Đổi hướng di chuyển.

        elif self.y + self.height / 2 > HEIGHT:  # Nếu đối tượng đi quá biên dưới...
            self.y = HEIGHT - self.height / 2  # Đặt lại vị trí của đối tượng.
            self.vel *= -1  # Đổi hướng di chuyển.

class Screen(p.sprite.Sprite):  # Định nghĩa một lớp mới có tên là Screen, là một lớp con của pygame.sprite.Sprite.
    def __init__(self):  # Đây là hàm khởi tạo cho lớp Screen.
        super().__init__()  # Gọi hàm khởi tạo của lớp cha Sprite.
        self.img1 = p.image.load('Scene.png')  # Tải hình ảnh 'Scene.png' và gán cho self.img1.
        self.img2 = p.image.load('You Win.png')  # Tải hình ảnh 'You Win.png' và gán cho self.img2.
        self.img3 = p.image.load('You lose.png')  # Tải hình ảnh 'You lose.png' và gán cho self.img3.

        self.img1 = p.transform.scale(self.img1,
                                      (WIDTH, HEIGHT))  # Thay đổi kích thước hình ảnh self.img1 thành WIDTHxHEIGHT.
        self.img2 = p.transform.scale(self.img2,
                                      (WIDTH, HEIGHT))  # Thay đổi kích thước hình ảnh self.img2 thành WIDTHxHEIGHT.
        self.img3 = p.transform.scale(self.img3,
                                      (WIDTH, HEIGHT))  # Thay đổi kích thước hình ảnh self.img3 thành WIDTHxHEIGHT.

        self.image = self.img1  # Gán hình ảnh hiện tại của đối tượng là self.img1.
        self.x = 0  # Tọa độ x của đối tượng.
        self.y = 0  # Tọa độ y của đối tượng.

        self.rect = self.image.get_rect()  # Lấy đối tượng Rect từ hình ảnh hiện tại của đối tượng.

    def update(self):  # Hàm cập nhật trạng thái của đối tượng.
        self.rect.topleft = (self.x, self.y)  # Cập nhật tọa độ góc trên bên trái của đối tượng Rect.

class Flag(p.sprite.Sprite):  # Định nghĩa một lớp mới có tên là Flag, là một lớp con của pygame.sprite.Sprite.
    def __init__(self, number):  # Đây là hàm khởi tạo cho lớp Flag.
        super().__init__()  # Gọi hàm khởi tạo của lớp cha Sprite.
        self.number = number  # Số thứ tự của cờ.

        if self.number == 1:  # Nếu số thứ tự của cờ là 1...
            self.image = p.image.load('point.png')  # Tải hình ảnh 'green flag.png' và gán cho self.image.
            self.visible = False  # Đặt trạng thái hiển thị của cờ là False.
            self.x = 50  # Tọa độ x của cờ.

        else:  # Nếu số thứ tự của cờ không phải là 1...
            self.image = p.image.load('point.png')  # Tải hình ảnh 'white flag.png' và gán cho self.image.
            self.visible = True  # Đặt trạng thái hiển thị của cờ là True.
            self.x = 1580  # Tọa độ x của cờ.

        self.y = HEIGHT / 2  # Tọa độ y của cờ.
        self.image = p.transform.scale(self.image,(50,50))  # Thay đổi kích thước hình ảnh của cờ thành gấp đôi.
        self.rect = self.image.get_rect()  # Lấy đối tượng Rect từ hình ảnh của cờ.
        self.mask = p.mask.from_surface(self.image)  # Tạo một đối tượng Mask từ hình ảnh của cờ.

    def update(self):  # Hàm cập nhật trạng thái của cờ.
        if self.visible:  # Nếu cờ đang hiển thị...
            self.collision()  # Gọi hàm kiểm tra va chạm.
            self.rect.center = (self.x, self.y)  # Cập nhật tọa độ trung tâm của đối tượng Rect.

    def collision(self):  # Hàm kiểm tra va chạm.
        global SCORE, cat  # Sử dụng biến toàn cục SCORE và cat.

        flag_hit = p.sprite.spritecollide(self, cat_group, False,
                                          p.sprite.collide_mask)  # Kiểm tra va chạm giữa đối tượng hiện tại và nhóm cat_group.
        if flag_hit:  # Nếu có va chạm...
            self.visible = False  # Đặt trạng thái hiển thị của đối tượng là False.

            if self.number == 1:  # Nếu số thứ tự của đối tượng là 1...
                white_flag.visible = True  # Đặt trạng thái hiển thị của white_flag là True.
                if SCORE <= 5:  # Nếu SCORE nhỏ hơn 5...
                    SwitchLevel()  # Gọi hàm SwitchLevel().

                else:  # Nếu SCORE không nhỏ hơn 5...
                    cat_group.empty()  # Xóa tất cả các đối tượng trong nhóm cat_group.
                    DeleteOtherItems()  # Gọi hàm DeleteOtherItems().

                    EndScreen(1)  # Gọi hàm EndScreen() với tham số là 1.

            else:  # Nếu số thứ tự của đối tượng không phải là 1...
                green_flag.visible = True  # Đặt trạng thái hiển thị của green_flag là True.

class Explosion(object):  # Định nghĩa một lớp mới có tên là Explosion.
    def __init__(self):  # Đây là hàm khởi tạo cho lớp Explosion.
        self.costume = 1  # Số thứ tự của hình ảnh hiện tại.
        self.width = 140  # Chiều rộng của hình ảnh.
        self.height = 140  # Chiều cao của hình ảnh.
        self.image = p.image.load(
            'explosion' + str(self.costume) + '.png')  # Tải hình ảnh 'explosion1.png' và gán cho self.image.
        self.image = p.transform.scale(self.image, (
        self.width, self.height))  # Thay đổi kích thước hình ảnh thành self.width x self.height.
        self.sound = p.mixer.Sound('e.mp3')  # Tải file âm thanh.
    def explode(self, x, y):  # Hàm tạo hiệu ứng nổ.
        x = x - self.width / 2  # Điều chỉnh tọa độ x.
        y = y - self.height / 2  # Điều chỉnh tọa độ y.
        DeleteCat()  # Gọi hàm DeleteCat().
        audio_playing = False
        self.sound.play()  # Phát âm thanh khi hiệu ứng nổ kích hoạt.

        while self.costume < 9:  # Trong khi số thứ tự của hình ảnh nhỏ hơn 9...
            self.image = p.image.load('explosion' + str(
                self.costume) + '.png')  # Tải hình ảnh 'explosion' kèm theo số thứ tự và gán cho self.image.
            self.image = p.transform.scale(self.image, (
            self.width, self.height))  # Thay đổi kích thước hình ảnh thành self.width x self.height.
            win.blit(self.image, (x, y))  # Vẽ hình ảnh lên cửa sổ tại vị trí (x, y).
            p.display.update()  # Cập nhật hiển thị.

            self.costume += 1  # Tăng số thứ tự của hình ảnh lên 1.
            time.sleep(0.1)  # Dừng chương trình trong 0.1 giây.

        DeleteOtherItems()  # Gọi hàm DeleteOtherItems().
        EndScreen(0)  # Gọi hàm EndScreen() với tham số là 0.

def ScoreDisplay():  # Hàm hiển thị điểm số.
    global gameOn  # Sử dụng biến toàn cục gameOn.

    if gameOn:  # Nếu game đang chạy...
        score_text = score_font.render('score' + str(SCORE) + ' / 5', True,
                                       (0, 0, 0))  # Tạo đối tượng TextSurface từ chuỗi 'score' + SCORE + ' / 5'.
        win.blit(score_text, (70,600))  # Vẽ đối tượng TextSurface lên cửa sổ tại vị trí (50, 10).

def checkFlags():  # Hàm kiểm tra các cờ.
    for flag in flags:  # Duyệt qua từng cờ trong danh sách flags.
        if not flag.visible:  # Nếu cờ không hiển thị...
            flag.kill()  # Gọi hàm kill() của cờ.

        else:  # Nếu cờ đang hiển thị...
            if not flag.alive():  # Nếu cờ không còn tồn tại trong nhóm...
                flag_group.add(flag)  # Thêm cờ vào nhóm flag_group.

def SwitchLevel():  # Hàm chuyển cấp độ.
    global SCORE  # Sử dụng biến toàn cục SCORE.

    if slow_car1.vel < 0:  # Nếu vận tốc của slow_car nhỏ hơn 0...
        slow_car1.vel -= 1  # Giảm vận tốc của slow_car đi 1.

    else:  # Nếu vận tốc của slow_car không nhỏ hơn 0...
        slow_car1.vel += 1  # Tăng vận tốc của slow_car lên 1.

    if fast_car1.vel < 0:  # Nếu vận tốc của fast_car nhỏ hơn 0...
        fast_car1.vel -= 1  # Giảm vận tốc của fast_car đi 1.

    else:  # Nếu vận tốc của fast_car không nhỏ hơn 0...
        fast_car1.vel += 1  # Tăng vận tốc của fast_car lên 1.

    SCORE += 1  # Tăng SCORE lên 1.

def DeleteCat():  # Hàm xóa con mèo.
    global cat  # Sử dụng biến toàn cục cat.

    cat.kill()  # Gọi hàm kill() của con mèo.
    screen_group.draw(win)  # Vẽ nhóm screen_group lên cửa sổ.
    car_group.draw(win)  # Vẽ nhóm car_group lên cửa sổ.
    flag_group.draw(win)  # Vẽ nhóm flag_group lên cửa sổ.

    screen_group.update()  # Cập nhật trạng thái của nhóm screen_group.
    car_group.update()  # Cập nhật trạng thái của nhóm car_group.
    flag_group.update()  # Cập nhật trạng thái của nhóm flag_group.

    p.display.update()  # Cập nhật hiển thị.

def DeleteOtherItems():  # Hàm xóa các đối tượng khác.
    car_group.empty()  # Xóa tất cả các đối tượng trong nhóm car_group.
    flag_group.empty()  # Xóa tất cả các đối tượng trong nhóm flag_group.
    flags.clear()  # Xóa tất cả các cờ trong danh sách flags.


def EndScreen(n):  # Hàm kết thúc màn hình.
    global gameOn  # Sử dụng biến toàn cục gameOn.

    gameOn = False  # Đặt trạng thái chạy của game là False.
    handle_audio()

    if n == 0:  # Nếu tham số n là 0...
        bg.image = bg.img3  # Thay đổi hình ảnh của bg thành bg.img3.

    elif n == 1:  # Nếu tham số n là 1...
        bg.image = bg.img2  # Thay đổi hình ảnh của bg thành bg.img2.

WIDTH = 1640  # Chiều rộng của cửa sổ.
HEIGHT = 1480  # Chiều cao của cửa sổ.

p.init()  # Khởi tạo Pygame.
p.mixer.init()
mixer.music.load('v.mp3')
mixer.music.play(-1)
win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Crossy Road')
clock = p.time.Clock()
# Load the audio icons
audio_on = p.image.load('on.png')
audio_off = p.image.load('off.png')
audio_on = p.transform.scale(audio_on, (50, 50))
audio_off = p.transform.scale(audio_off, (50, 50))

# Variable to track audio state
audio_playing = True

# Function to handle audio
def handle_audio():  # Hàm xử lý âm thanh.
    global audio_playing  # Sử dụng biến toàn cục audio_playing.
    if audio_playing:  # Nếu âm thanh đang phát...
        mixer.music.pause()  # Tạm dừng âm thanh.
        audio_playing = False  # Đặt trạng thái phát âm thanh là False.

    else:  # Nếu âm thanh không phát...
        mixer.music.unpause()  # Tiếp tục phát âm thanh.
        audio_playing = True  # Đặt trạng thái phát âm thanh là True.

SCORE = 0  # Điểm số ban đầu.
score_font = p.font.SysFont('comicsans', 40, True)  # Font chữ và kích thước chữ cho điểm số.

bg = Screen()  # Tạo một đối tượng Screen.
screen_group = p.sprite.Group()  # Tạo một nhóm sprite.
screen_group.add(bg)  # Thêm đối tượng Screen vào nhóm.

cat = Cat()  # Tạo một đối tượng Cat.
cat_group = p.sprite.Group()  # Tạo một nhóm sprite.
cat_group.add(cat)  # Thêm đối tượng Cat vào nhóm.

slow_car1 = Car(1)  # Tạo một đối tượng Car với số thứ tự là 1.
fast_car1 = Car(2)
slow_car2 = Car(3)
fast_car2 = Car(4)

# Tạo một đối tượng Car với số thứ tự là 2.
car_group = p.sprite.Group()  # Tạo một nhóm sprite.
car_group.add(slow_car1, fast_car1, slow_car2, fast_car2)  # Thêm các đối tượng Car vào nhóm.

green_flag = Flag(1)  # Tạo một đối tượng Flag với số thứ tự là 1.
white_flag = Flag(2)  # Tạo một đối tượng Flag với số thứ tự là 2.
flag_group = p.sprite.Group()  # Tạo một nhóm sprite.
flag_group.add(green_flag, white_flag)  # Thêm các đối tượng Flag vào nhóm.
flags = [green_flag, white_flag]  # Tạo một danh sách chứa các đối tượng Flag.

explosion = Explosion()  # Tạo một đối tượng Explosion.


def display_menu():  # Function to display the menu
    menu_image = p.image.load('map2.png')  # Tải hình ảnh menu.

    menu_font = p.font.SysFont('comicsans', 60, True)
    title = menu_font.render('Crossy Road', True, (0, 0, 0))
    instruction = menu_font.render('Press SPACE to start', True, (0, 0, 0))
    win.blit(menu_image, (400 , 480)) # Vẽ hình ảnh menu lên cửa sổ game.
    win.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    win.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT // 2))
gameOn = False  # Trạng thái chạy của game.
run = True  # Biến điều khiển vòng lặp chính của game.
def game_loop():
    global run, gameOn
    while run:  # Vòng lặp chính của game.
        clock.tick(60)  # Đặt tốc độ cập nhật của game là 60 FPS.
        for event in p.event.get():  # Duyệt qua tất cả các sự kiện.
            if event.type == p.QUIT:  # Nếu sự kiện thoát game...
                run = False  # Kết thúc vòng lặp chính.
            if event.type == p.MOUSEBUTTONDOWN:  # Nếu sự kiện nhấn chuột...
                x, y = p.mouse.get_pos()  # Lấy tọa độ của con trỏ chuột.
                # Kiểm tra xem biểu tượng âm thanh có được nhấn không.
                if 70 <= x <= 160 and 900 <= y <= 1200:
                    handle_audio()  # Gọi hàm xử lý âm thanh.


        win.fill((0, 255, 0))  # Đổ màu nền cho cửa sổ game.



        screen_group.draw(win)  # Vẽ nhóm screen_group lên cửa sổ game.

        ScoreDisplay()  # Gọi hàm hiển thị điểm số.
        checkFlags()  # Gọi hàm kiểm tra các cờ.

        car_group.draw(win)  # Vẽ nhóm car_group lên cửa sổ game.
        cat_group.draw(win)  # Vẽ nhóm cat_group lên cửa sổ game.
        flag_group.draw(win)  # Vẽ nhóm flag_group lên cửa sổ game.
        # Vẽ biểu tượng âm thanh phù hợp.
        if audio_playing:  # Nếu âm thanh đang phát...
            win.blit(audio_on, (70,900))  # Vẽ biểu tượng âm thanh bật.

        else:  # Nếu âm thanh không phát...
            win.blit(audio_off, (70, 900))  # Vẽ biểu tượng âm thanh tắt.
        car_group.update()  # Cập nhật trạng thái của nhóm car_group.
        cat_group.update()  # Cập nhật trạng thái của nhóm cat_group.
        flag_group.update()  # Cập nhật trạng thái của nhóm flag_group.

        screen_group.update()  # Cập nhật trạng thái của nhóm screen_group.

        p.display.update()  # Cập nhật hiển thị.

gameOn = False  # Set gameOn to False initially
while True:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()

    keys = p.key.get_pressed()
    if keys[p.K_SPACE]:  # If space key is pressed, start the game
        gameOn = True

    win.fill((0, 255, 0))  # Fill the window with green color

    if gameOn:
        game_loop()  # Start the game loop when gameOn is True
    else:
        display_menu()  # Display the menu when gameOn is False

    p.display.update()