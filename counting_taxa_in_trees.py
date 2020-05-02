# This script counts the number of times a certain taxon appears in a phylogenetic tree; input files are a list of the trees that should be checked as well as a list of taxa

import os

ogs = open("OGs", "r").readlines()
#ogs = ["OG5_126572", "OG5_126573", "OG5_126595", "OG5_126605", "OG5_126611", "OG5_126631"]

for og in ogs:
	results = ""
	og = og.replace("\n", "")

	#mcs = ["Op","Pl","Sr","Am","EE","Ex","Ba","Za"] 
	#mcs = ["Am_ar", "Am_di", "Am_hi", "Am_is", "Am_my", "Am_th", "Am_tu", "Am_va", "EE_ap", "EE_br", "EE_ce", "EE_cr", "EE_ha", "EE_ka", "Ex_eu", "Ex_fo", "Ex_he", "Ex_is", "Ex_ja", "Ex_ma", "Ex_ox", "Ex_pa", "Op_ch", "Op_fu", "Op_ic", "Op_me", "Pl_gl", "Pl_rh", "Pl_gr", "Sr_ap", "Sr_ch", "Sr_ci", "Sr_di", "Sr_pe", "Sr_rh", "Sr_st", "Za_as", "Za_ba", "Za_cr", "Za_ea", "Za_eb", "Za_ec", "Za_eh", "Za_em", "Za_ep", "Za_et", "Za_ey", "Za_ko", "Za_na", "Za_th", "Ba_th", "Ba_fc", "Ba_fb", "Ba_de", "Ba_cy", "Ba_ch", "Ba_ac", "Ba_sp", "Ba_pl", "Ba_cd", "Ba_pg", "Ba_pd", "Ba_pb", "Ba_pa", "Ba_ni", "Ba_fu", "Ba_ba", "Ba_di", "Ba_aq"] 
	mcs = ["Am_ar_ehis", "Am_ar_einv", "Am_ar_Mbal", "Am_di_Acas", "Am_di_Endo", "Am_di_Mspa", "Am_di_Patl", "Am_di_Pcat", "Am_di_Pess", "Am_di_Tric", "Am_di_Vexi", "Am_di_Vrob", "Am_hi_Gfon", "Am_is_Fnol", "Am_is_Sram", "Am_my_Asub", "Am_my_ddis", "Am_my_Ppol", "Am_th_Tqua", "Am_tu_Hpcb", "Am_tu_Hscb", "Am_tu_Lscb", "Am_tu_Ntcb", "Am_tu_Qscb", "Am_va_Usch", "EE_ap_Asig", "EE_ap_Nlon", "EE_ap_Ftro", "EE_br_Bant", "EE_ce_Reri", "EE_ce_Rhet", "EE_cr_Ccur", "EE_cr_Gspb", "EE_cr_Hand", "EE_cr_Htep", "EE_cr_Gspa", "EE_cr_Hphi", "EE_cr_Gcry", "EE_cr_Gthe", "EE_cr_Rlen", "EE_ha_Clep", "EE_ha_Pcar", "EE_ha_Ispa", "EE_ha_Ehux", "EE_ha_Plut", "EE_ha_Pant", "EE_ha_Cpol", "EE_ha_Ppar", "EE_ka_Rtru", "EE_ha_Saps", "Ex_eu_Bsal", "Ex_eu_Egra", "Ex_eu_lbra", "Ex_eu_linf", "Ex_eu_Lpyr", "Ex_eu_Ndes", "Ex_eu_Pemi", "Ex_eu_Scul", "Ex_eu_tbru", "Ex_eu_tcon", "Ex_eu_tcru", "Ex_eu_tviv", "Ex_fo_glae", "Ex_fo_Ssal", "Ex_he_Ngru", "Ex_he_Pcos", "Ex_is_Tpyr", "Ex_ja_Rame", "Ex_ja_Secu", "Ex_ma_Mcal", "Ex_ma_Mjak", "Ex_ox_Mono", "Ex_pa_Hmel", "Ex_pa_Phom", "Ex_pa_tvag", "Op_ch_Mova", "Op_ch_Sros", "Op_fu_Amac", "Op_fu_Gpro", "Op_fu_Rall", "Op_fu_aory", "Op_fu_scer", "Op_fu_spom", "Op_fu_cneg", "Op_fu_eint", "Op_fu_Rdel", "Op_fu_Pspa", "Op_fu_Ccor", "Op_ic_Cowc", "Op_ic_Sarc", "Op_me_drer", "Op_me_mmus", "Op_me_hsap", "Op_me_sman", "Op_me_cele", "Op_me_dmel", "Op_me_Acal", "Op_me_Hvul", "Op_me_Lcha", "Op_me_Aque", "Pl_gl_Cglo", "Pl_gl_Gwit", "Pl_rh_Pyez", "Pl_rh_Paer", "Pl_rh_Ccoe", "Pl_rh_Ccho", "Pl_rh_Rmac", "Pl_rh_Rmar", "Pl_gr_Tstr", "Pl_gr_crei", "Pl_gr_vcar", "Pl_gr_otau", "Pl_gr_micr", "Pl_gr_Pcol", "Pl_gr_Cvar", "Pl_gr_Pspa", "Pl_gr_Corb", "Pl_gr_ppat", "Pl_gr_Mpol", "Pl_gr_Gbil", "Pl_gr_Cjap", "Pl_gr_Atri", "Pl_gr_rcom", "Pl_gr_atha", "Pl_gr_osat", "Sr_ap_bbov", "Sr_ap_cmur", "Sr_ap_Eten", "Sr_ap_pviv", "Sr_ap_tgon", "Sr_ch_Vbra", "Sr_ci_Br01", "Sr_ci_Btcb", "Sr_ci_Dmcb", "Sr_ci_tthe", "Sr_ci_Cucb", "Sr_ci_Otri", "Sr_ci_Scer", "Sr_ci_Lx11", "Sr_di_Aspi", "Sr_di_Pret", "Sr_di_Gcat", "Sr_di_Kbre", "Sr_di_Omar", "Sr_di_Dbal", "Sr_di_Stro", "Sr_di_Pmin", "Sr_di_Smic", "Sr_pe_Olen", "Sr_pe_Perk", "Sr_rh_Bmot", "Sr_rh_Lamo", "Sr_rh_Crep", "Sr_rh_Pglo", "Sr_rh_Loce", "Sr_rh_Nsph", "Sr_rh_Bnat", "Sr_rh_Blon", "Sr_rh_Gspa", "Sr_rh_Pbra", "Sr_rh_Spsu", "Sr_rh_Eucb", "Sr_rh_Lvor", "Sr_rh_Adcb", "Sr_rh_Recb", "Sr_rh_Qjcb", "Sr_rh_Sspa", "Sr_rh_Pacb", "Sr_rh_Emar", "Sr_rh_Hgcb", "Sr_rh_Amcb", "Sr_rh_Micb", "Sr_rh_Trcb", "Sr_rh_Pina", "Sr_rh_Cten", "Sr_st_Paus", "Sr_st_Ptri", "Sr_st_Stur", "Sr_st_tpse", "Sr_st_Arad", "Sr_st_Suni", "Sr_st_Espi", "Sr_st_Dbri", "Sr_st_Cspa", "Sr_st_Bhom", "Sr_st_Bpac", "Sr_st_Ospa", "Sr_st_Pves", "Sr_st_Fpar", "Sr_st_Pter", "Sr_st_Alim", "Sr_st_pram", "Sr_st_Sdic", "Sr_st_Alag", "Sr_st_Cfra", "Sr_st_Ppyr", "Sr_st_Esil", "Sr_st_Csub", "Sr_st_Spus", "Sr_st_Mspa", "Za_as_Heia", "Za_as_Loki", "Za_as_Odin", "Za_as_Thob", "Za_ba_Crea", "Za_cr_Ahos", "Za_cr_msed", "Za_cr_Pfum", "Za_cr_Pogu", "Za_cr_smar", "Za_cr_ssol", "Za_ea_aful", "Za_eb_Mspa", "Za_ec_Minf", "Za_eh_Haci", "Za_eh_Hlai", "Za_eh_Hmar", "Za_eh_Hsol", "Za_em_Mhol", "Za_ep_tvol", "Za_et_Tkod", "Za_ey_Mkan", "Za_ko_ckor", "Za_na_nequ", "Za_th_Csym", "Ba_th_tmar", "Ba_fc_Oval", "Ba_fb_bant", "Ba_de_Trad", "Ba_cy_Syel", "Ba_cy_Onig", "Ba_cy_Acyl", "Ba_ch_Caur", "Ba_ac_Cdip", "Ba_sp_Sple", "Ba_pl_rbal", "Ba_cd_Cmur", "Ba_pg_vcho", "Ba_pg_ypes", "Ba_pg_ecol", "Ba_pd_Hoch", "Ba_pd_Daes", "Ba_pb_bmal", "Ba_pa_rpro", "Ba_pa_Bjap", "Ba_ni_Tyel", "Ba_fu_Fnuc", "Ba_ba_Bfra", "Ba_di_Dtur", "Ba_aq_aaeo"] 
	for mc in mcs:
		tree = open("/Users/katzlab_agnes/Desktop/Final_epi_trees/smart/counting_again/trees/RAxML_bestTree." + og + "_postguidance.fas_renamed.tre", 'r').readline()
#		tree = open("trees/RAxML_bestTree." + og + "_postguidance.fas_renamed.tre", 'r').readline()
		tree = tree.split(",")
		count = 0
		taxa = []
		count_taxa = 0
	 

		for tip in tree:
			tip = tip.replace("(", "")

		# way 1 #
		#	tip = tip.split("_")
		#	clade = tip[0] + "_" + tip[1] + "_" + tip[2]
		#	print clade
	
		# way 2 #
			clade = tip[0:10]
			taxa.append(clade)
		
			if clade.startswith(mc):
				count = count + 1

		taxa = list(set(taxa))
	
		for taxon in taxa:
			if taxon.startswith(mc):
				count_taxa = count_taxa + 1
	
			
		results = results + "," + str(count) + "," + str(count_taxa) 
	
	print og + "," + results
			
			
	
	
