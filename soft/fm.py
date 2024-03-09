import os

with open("/home/denchik/develop/logo/parents.html", "r+") as f:
    print("Введите название пособия:")
    name = input()
    print("Введите название файла:")
    upload = input()
    part = f.read()
    print(part)
    l = len(part)
    f.seek(l + 46)
    f.seek(l + 46)
    f.write("\n")
    f.write('                <li style="margin-bottom: 3%;">\n                    <div class="task_block">\n                        <div class="data_text"><p>' + name + '</p></div>\n                        <form action="data/' + upload + '" style="float: right;">\n                            <button class="custom-btn btn-5" href="data/figure.odt"><span\n                                    style="font-size: 17px;">Скачать</span></button>\n                        </form>\n                    </div>\n                </li>\n')
    f.write('\n            </ul>\n        </div>\n    </div>\n</body>\n</html>')

os.system("git add ..")
os.system("git status")
os.system('git commit -m "auto add ' + name + ' in parents"')
os.system("git pull")
os.system("git push -u origin main")
print("Готово")