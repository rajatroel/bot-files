clear
touch ~/.bashrc
grep -qxF 'clear' ~/.bashrc || echo 'clear' >> ~/.bashrc
echo -e "\e[1;36mPreparing system! please don't close the app...\e[0m"
curl -# -L https://github.com/rajatroel/bot-files/releases/download/v1.0/termux-64bit-backup.tar.gz -o /storage/emulated/0/backup.tar.gz 2>&1 | while read -d $'\r' line; do
  pct=$(echo "$line" | grep -o '[0-9.]*%')
  if [ ! -z "$pct" ]; then
    echo -ne "\r\e[0KDownloading files : $pct"
  fi
done
echo -e "\n\e[1;36mExtracting environment (this may take a few minutes)...\e[0m"
tar -zxf /storage/emulated/0/backup.tar.gz -C /data/data/com.termux/files
rm -f /storage/emulated/0/backup.tar.gz
echo 'SUCCESS' > /storage/emulated/0/termux_ready.txt
echo -e "\e[1;32mSetup complete! Exiting...\e[0m"
sleep 2
exit
