clear all
set more off
capture log close

/*==============================================================================

Makalah Akhir Analisis Empiris Organisasi Industri
Title			: Estimasi Fungsi Produksi Idustri Pakaian Jadi (Konveksi) dari Tekstil
Approach		: ACF2015
Author			: Ludy Hasby Aulia, Dr. Ashintya Damayati
Version			: 31 Des 2024
==============================================================================*/
// set global work dir 
global workdir "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper"
cd "$workdir"

// dataset loading
use SI2011-2015, clear

set seed 1234 // set random seed to reproducable code 

// keep selected industry, please replace 10431 with your disired DISIC5
keep if (DISIC5=="14111")

// set x dan time (individual: PSID, time=year)
xtset PSID year

/// Pemilihan Variabel
keep PSID year DPROVI DKABUP OUTPUT YPRVCU VTLVCU LTLNOU V1101 V1103 V1106 V1109 V1112 V1115 CBNECU CMNECU CVNECU CONECU CTNECU ENPKHU EPLKHU RTLVCU IINPUT

/// Deflasikan dengan Indeks Harga, Pendefinisian indeks harga
// IHPB Akhir dengan base 2010, sumber publikasi BPS
gen IHPBAkh=.
replace IHPBAkh= 106.3352 if year==2011
replace IHPBAkh= 112.055 if year==2012
replace IHPBAkh= 103.88 if year==2013
replace IHPBAkh= 132.37 if year==2014
replace IHPBAkh= 152.11 if year==2015

// IHPB Antara dengan base 2010, sumber publikasi BPS
gen IHPBAnt=.
replace IHPBAnt= 105.483 if year==2011
replace IHPBAnt= 110.122 if year==2012
replace IHPBAnt= 119.6 if year==2013
replace IHPBAnt= 126 if year==2014
replace IHPBAnt= 124.75 if year==2015

// IHPB Mentah dengan base 2010, sumber publikasi BPS
gen IHPBMent=.
replace IHPBMent= 109.35 if year==2011
replace IHPBMent= 115.2485 if year==2012
replace IHPBMent= 117.08 if year==2013
replace IHPBMent= 138.96 if year==2014
replace IHPBMent= 163.01 if year==2015

// IHK dengan base 2007, sumber publikasi BPS
gen IHK=.
replace IHK= 127.45 if year==2015
replace IHK= 132.9 if year==2014
replace IHK= 142.18 if year==2013
replace IHK= 150.46 if year==2012
replace IHK= 160.0382 if year==2011

*Generating and Cleaning Investment and Intermediate Input Data
gen rOUTPUT = OUTPUT/IHPBAkh*100
gen rPROD = YPRVCU/IHPBAkh*100
gen rVA = VTLVCU/IHK*100
ren LTLNOU LABOR
gen CAPITAL = V1115/IHPBAnt
gen CAPElec = ENPKHU + EPLKHU
gen IHPBmat = (IHPBMent + IHPBAnt)/2
gen MATERIAL = RTLVCU/IHPBmat*100

*Generating and Cleaning Investment and Intermediate Input Data
gen rIINPUT = IINPUT/IHPBmat*100
gen rINVEST = d.CAPITAL

*Generating Logarithmic Variables
gen y = ln(rOUTPUT)
gen va = ln(rVA)
gen l = ln(LABOR)
gen k = ln(CAPElec)
gen m = ln(rIINPUT)
gen i = ln(rINVEST)
replace i=0 if rINVEST==0

/// Ekspor untuk eksplorasi lebih lanjut pada Software yang lain
export delimited using "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper\eksplorasi_pre.csv", replace

clear all
set more off
capture log close
/// Import dataset pasca eksploratif
import delimited "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper\post_eksplorasi.csv", clear

///Ackerberg Caves Frazer (2015)
*Value Added
// Translog
prodest va, method(lp) free(l) proxy(m) state(k) acf va att trans id(psid) t(year) poly(2) fsresiduals(residacftrans_va)
predict TFPacftrans_va, resid
egen meanTFPacftrans_va = mean(TFPacftrans_va), by (year)
sort year
twoway line meanTFPacftrans_va year, title("Grafik Rerata TFP Translog-VA antar Tahun")
graph export "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper\plot_sta
> ta\translog-va.png", as(png) name("translog-va")
// Cobb-Douglas
prodest va, method(lp) free(l) proxy(m) state(k) acf va att id(psid) t(year) fsresiduals(residacfcd_va)
predict TFPacfcd_va, resid
egen meanTFPacfcd_va = mean(TFPacfcd_va), by (year)
sort year
twoway line meanTFPacfcd_va year, title("Grafik Rerata TFP CD-VA antar Tahun")
graph export "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper\plot_sta
> ta\cd-va.png", as(png) name("cd-va")

*Gross Output
gen va_copy = va
drop va
gen va = y
// Cobb-Douglas
prodest va, method(lp) free(l) proxy(m) state(k) acf va att id(psid) t(year) fsresiduals(residacfcd_go)
predict TFPacfcd_go, resid
egen meanTFPacfcd_go = mean(TFPacfcd_go), by (year)
sort year
twoway line meanTFPacfcd_go year, title("Grafik Rerata TFP CD-GO antar Tahun")
graph export "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper\plot_sta
> ta\cd-go.png", as(png) name("cd-go")
// Translog
prodest va, method(lp) free(l) proxy(m) state(k) acf va att trans id(psid) t(year) poly(2) fsresiduals(residacftrans_go)
predict TFPacftrans_go, resid
egen meanTFPacftrans_go = mean(TFPacftrans_go), by (year)
sort year
twoway line meanTFPacftrans_go year, title("Grafik TFP Translog-GO antar Tahun")
graph export "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper\plot_sta
> ta\translog-go.png", as(png) name("translog-go")

// kembalikan va asli
drop va
gen va = va_copy
drop va_copy

/// multiline plot 
line meanTFPacfcd_va meanTFPacftrans_va meanTFPacfcd_go meanTFPacftrans_go year, legend(size(medsmall)) title("Kompilasi Rerata ln(TFP) dengan ACF")
// va dan hasil prediksi
egen mean_va = mean(va), by(year)
line mean_va meanTFPacfcd_va meanTFPacftrans_va year, legend(label(1 "Aktual VA") label(2 "CD-VA") label(3 "Translog-VA")) title("Prediksi VS Aktual Nilai Tambah (va)")
// va dan hasil prediksi
egen mean_y = mean(y), by(year)
line mean_y meanTFPacfcd_go meanTFPacftrans_go year, legend(label(1 "Aktual GO") label(2 "CD-GO") label(3 "Translog-GO")) title("Prediksi VS Aktual Nilai Tambah (va)")

		   
*Productivity Level
gen TFPlvACFcd_va = exp(TFPacfcd_va)
gen TFPlvACFtrans_va = exp(TFPacftrans_va)
egen meanTFPlvACFcd_va = mean(TFPlvACFcd_va), by (year)
egen meanTFPlvACFtrans_va = mean(TFPlvACFtrans_va), by (year)

gen TFPlvACFcd_go = exp(TFPacfcd_go)
gen TFPlvACFtrans_go = exp(TFPacftrans_go)
egen meanTFPlvACFcd_go = mean(TFPlvACFcd_go), by (year)
egen meanTFPlvACFtrans_go = mean(TFPlvACFtrans_go), by (year)

twoway line meanTFPlvACFcd_va year, title("TFP CD-VA")
twoway line meanTFPlvACFtrans_va year, title("TFP Translog-VA")
twoway line meanTFPlvACFcd_go year, title("TFP CD-GO")
twoway line meanTFPlvACFtrans_go year, title("TFP Translog-GO")

export delimited using "C:\Users\Pongo\Documents\pribadi\ilmu_ekonomi\organisasi_industri\final_paper\post_prediction.csv", replace
save SI2011-2015_post_modelling, replace