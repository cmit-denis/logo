import os
print("Введите название пособия")
name = input()
print("Введите название файла")
upload = input()
with open("/home/denis/webs/logo/parents.html", "r+") as f:
    part = f.read()
    print(part)
    l = len(part)
    f.seek(l + 46)
    f.seek(l + 46)
    f.write("\n")
    f.write('                <li style="margin-bottom: 3%;">\n                    <div class="task_block">\n                        <p style="float: left; font-size: large;">' + name + '</p>\n                        <form action="data/' + upload + '" style="float: right;">\n                            <button class="custom-btn btn-5" href="data/figure.odt"><span\n                                    style="font-size: 17px;">Скачать</span></button>\n                        </form>\n                    </div>\n                </li>\n')
    f.write('\n            </ul>\n        </div>\n    </div>\n</body>\n</html>')

os.system("git add /home/denis/webs/logo")
os.system("git status")
os.system('git commit -m "auto add ' + name + '"')
os.system("git pull")
os.system(" git push -u origin main")
print("Готово")