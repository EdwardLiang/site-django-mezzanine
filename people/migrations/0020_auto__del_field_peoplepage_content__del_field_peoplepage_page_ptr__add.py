# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PeoplePage.content'
        db.delete_column(u'people_peoplepage', 'content')

        # Deleting field 'PeoplePage.page_ptr'
        db.delete_column(u'people_peoplepage', u'page_ptr_id')

        # Adding field 'PeoplePage.catalystpage_ptr'
        db.add_column(u'people_peoplepage', u'catalystpage_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2014, 6, 25, 0, 0), to=orm['custom.CatalystPage'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PeoplePage.content'
        db.add_column(u'people_peoplepage', 'content',
                      self.gf('mezzanine.core.fields.RichTextField')(default=' '),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'PeoplePage.page_ptr'
        raise RuntimeError("Cannot reverse this migration. 'PeoplePage.page_ptr' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'PeoplePage.page_ptr'
        db.add_column(u'people_peoplepage', u'page_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'PeoplePage.catalystpage_ptr'
        db.delete_column(u'people_peoplepage', u'catalystpage_ptr_id')


    models = {
        u'custom.catalystpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'CatalystPage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'font_awesome_icon': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'navbar_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'title_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'people.membercategory': {
            'Meta': {'ordering': "('title',)", 'object_name': 'MemberCategory'},
            'heading_bar_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': u"orm['people.PeoplePage']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'people.peoplepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PeoplePage', '_ormbases': [u'custom.CatalystPage']},
            u'catalystpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['custom.CatalystPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'people.person': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Person'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'bio': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'people'", 'blank': 'True', 'to': u"orm['people.MemberCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': u"orm['people.PeoplePage']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['people']