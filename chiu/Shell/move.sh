
local_date=$(date +"%Y%m%d%H/%M")
mkdir /mnt/sdc/Data2018-07-12/Data-$local_date
/bin/find /mnt/sdb/data/ -type -f name '*.zip' -exec mv {} /mnt/sdc/Data2018-07-12/Data-$local_date/ \