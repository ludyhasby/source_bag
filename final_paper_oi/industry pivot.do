clear all
set more off
capture log close

// work dir 
global workdir "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper"
// dataset loading
use SI2011-2015, clear

// 	/// look PSID that consistent on survei 2011-2015
// 	// tag psid unik untuk setiap tahun 
// 	egen tag = tag(PSID year)
// 	// jumlah tahun untuk setiap psid
// 	bysort PSID (year): gen count_tahun = sum(tag)
// 	// filter psid yang ada di 2011-2015
// 	keep if (count_tahun == 5)

// make variabel that count PSID base on DISIC5
egen jumlah_PSID = count(PSID), by(DISIC5 year)
// keep DISIC5 and jumlah_PSID
keep DISIC5 year jumlah_PSID	
// drop duplicates 
duplicates drop DISIC5 jumlah_PSID, force
// reshape 
reshape wide jumlah_PSID, i(DISIC5) j(year)
// rename 
rename jumlah_PSID2011 jumlah_PSID_2011
rename jumlah_PSID2012 jumlah_PSID_2012
rename jumlah_PSID2013 jumlah_PSID_2013
rename jumlah_PSID2014 jumlah_PSID_2014
rename jumlah_PSID2015 jumlah_PSID_2015
// sort by jumlah_PSID_2011
gsort -jumlah_PSID_2011

// 	/// untuk lihat psid yang konsisten saja 
// 	gsort -jumlah_PSID2015
	
// show top 10 
list in 1/10
// keep top 10
keep in 1/10
// save
export delimited using "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\session_9\Solusi_Tugas_9\Dataset\top_industry.csv", replace
