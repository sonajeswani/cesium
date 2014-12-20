#!/usr/bin/env python
""" test_feature_algorithms.py

NOTE:
 - Requires system environment variable: TCP_DIR
     - This is the full path of the top directory of TCP project
     - In other words, the TCP directory which was svn checked-out
     - e.g. .bashrc/execute for bash:
                export TCP_DIR=/home/pteluser/src/TCP/
"""

import os, sys
import warnings
warnings.simplefilter("ignore",DeprecationWarning) 

sys.path.append(os.path.abspath(os.environ.get("TCP_DIR") + \
                                      'Software/feature_extract'))
sys.path.append(os.path.abspath(os.environ.get("TCP_DIR") + \
              'Software/feature_extract/Code'))
from Code import *
import db_importer

signals_list = []
gen = generators_importers.from_xml(signals_list)

### Single filter, many datapoint:
#gen.generate(xml_handle="../../Data/vosource_9026.xml")
if 0:
    sys.path.append(os.path.abspath(os.environ.get("TCP_DIR") + \
                                    'Software/ingest_tools'))
    from get_colors_for_tutor_sources import Parse_Nomad_Colors_List
    # NOTE: can load this and datastructure once for speed:
    ParseNomadColorsList = Parse_Nomad_Colors_List(fpath=os.path.abspath(os.environ.get("TCP_DIR") + '/Data/best_nomad_src_list'))

#xml_str = open("/Data/dstarr/Data/historical_archive_featurexmls_arffs/tutor_126/2011-02-06_00:03:02.699641/xmls/100263871.xml").read()
#xml_str = open(os.path.expandvars("$HOME/src/TCP/Data/vosource_9026.xml")).read()
#xml_str = open("/global/homes/d/dstarr/src/TCP/Data/100263871.xml").read()
#xml_str = open("/home/isaac/Working/Research/code/scratch/230049.xml").read()
#xml_str = open("../../Data/vosource_9026.xml").read()
xml_str = open("/big_data/dstarr/Data/asas_ACVS_50k_new_aper_20120221/100244888.xml").read()
#xml_str = open("/media/raid_0/historical_archive_featurexmls_arffs/tutor_126/2011-02-06_00:03:02.699641/xmls/100233074.xml").read()

if 0:
    new_xml_str = ParseNomadColorsList.get_colors_for_srcid(xml_str=xml_str, srcid=263871)
    gen.generate(xml_handle=new_xml_str)
gen.generate(xml_handle=xml_str)

#gen.generate(xml_handle="/media/raid_0/historical_archive_featurexmls_arffs/tutor_126/2011-02-06_00:03:02.699641/xmls/100255056.xml")
#gen.generate(xml_handle="/home/pteluser/scratch/Noisification/jsb_classified_xmls/6930531.xml")
#gen.generate(xml_handle="/tmp/100017394_3.36224385129.xml")
#gen.generate(xml_handle=os.path.expandvars("/global/home/users/dstarr/scratch/vosource_xml_writedir/100164341.xml"))
#gen.generate(xml_handle=os.path.expandvars("$HOME/Dropbox/Public/work/100148014.xml"))
#gen.generate(xml_handle=os.path.expandvars("$HOME/Dropbox/Public/work/100148014.xml"))
#gen.generate(xml_handle="/tmp/vosource_test.xml")

#gen.generate(xml_handle='/tmp/111/vosource.PTF09h.xml')
# #gen.generate(xml_handle=os.path.expandvars("$TCP_DIR/Data/vosource_tutor12881.xml"))
# #import cPickle
# #cPickle.dump(gen.signals_list,open(os.path.expandvars("$TCP_DIR/Data/vosource_tutor12881.signal_properties.pkl"),'w'),cPickle.HIGHEST_PROTOCOL)
# #sys.exit()
### Multi filter SDSS source:
#gen.generate(xml_handle="../../Data/source_5.xml")
### Single difference object sample of pseudo PTF:
#gen.generate(xml_handle="../../Data/ptf_1diffobj_vosource.xml")

if 0:
    ### Sigma clipping example:
    from data_cleaning import sigmaclip_sdict_ts
    sigma = 1
    print(sigma, 'before:', len(gen.sig.x_sdict['ts']['V']['m']))
    sigmaclip_sdict_ts(gen.sig.x_sdict['ts'], sigma_low=sigma, sigma_high=sigma)
    print(sigma, 'after:', len(gen.sig.x_sdict['ts']['V']['m']))

gen.sig.add_features_to_xml_string(gen.signals_list)

#feature_added_VOSource_XML_fpath = '/home/isaac/Working/Research/code/scratch/vosource_out.xml'
feature_added_VOSource_XML_fpath = '/tmp/vosource_out.xml'
#gen.sig.write_xml(out_xml_fpath=feature_added_VOSource_XML_fpath)
gen.sig.write_xml(out_xml_fpath=feature_added_VOSource_XML_fpath)
print("Wrote VOSource XML (with features) to:", feature_added_VOSource_XML_fpath)

#print "signals_list[0].properties['data'].keys()"
#for f in signals_list[0].properties['data'].keys():
#    print (signals_list[0].properties['data'][f]['features'],f)

#print "gal b value:", signals_list[0].properties['data']['multiband']['features']['galb'], signals_list[0].properties['data']['multiband']['features']['galb'].why
#print "gal l value:", signals_list[0].properties['data']['multiband']['features']['gall'], signals_list[0].properties['data']['multiband']['features']['gall'].why
#print "ecp b value:", signals_list[0].properties['data']['multiband']['features']['ecpb'], signals_list[0].properties['data']['multiband']['features']['ecpb'].why
#print "ecp l value:", signals_list[0].properties['data']['multiband']['features']['ecpl'], signals_list[0].properties['data']['multiband']['features']['ecpl'].why

for signal in signals_list:
    #obsolete#print "firstr", signal.properties['data']['r']['features']['first_freq']
    #obsolete#print "firstu", signal.properties['data']['u']['features']['first_freq']
    #print "ws_variability_ru value"
    #print signal.properties['data']['multiband']['features']['ws_variability_ru']
    #print signal.properties['data']['multiband']['features']['ws_variability_ru'].why
    pass
    # NED extracted features:
    #print 'dist_arcmin', signal.properties['data']['multiband']['features']['distance_in_arcmin_to_nearest_galaxy']
    #print 'dist_kpc', signal.properties['data']['multiband']['features']['distance_in_kpc_to_nearest_galaxy']


    # TODO: eventually use unittest module for tests:
    #chi2_val = signal.properties['data']['r']['features']['chi2']
#print chi2_val
#if str(chi2_val) == '1131154.65019':
#    print "\n\nSimple TEST = OK\n"

