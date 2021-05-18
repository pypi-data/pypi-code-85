"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
# Generated by Django 3.1.4 on 2021-03-03 10:37

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('tasks', '0001_initial'), ('tasks', '0002_task_meta'), ('tasks', '0003_auto_20190328_1641'), ('tasks', '0003_auto_20190327_1906'), ('tasks', '0004_merge_20190329_1219'), ('tasks', '0005_auto_20190506_1532'), ('tasks', '0006_task_exposed'), ('tasks', '0007_auto_20190621_1106'), ('tasks', '0008_auto_20190621_1426'), ('tasks', '0009_remove_taskcompletion_was_generated'), ('tasks', '0010_auto_20190813_2215'), ('tasks', '0011_taskcompletion_updates_history'), ('tasks', '0012_auto_20190921_0830'), ('tasks', '0013_auto_20190925_1602'), ('tasks', '0014_auto_20191002_1002'), ('tasks', '0015_taskcompletion_lead_time'), ('tasks', '0016_completionpairwisestats'), ('tasks', '0017_task_taken_at'), ('tasks', '0018_auto_20200202_2017'), ('tasks', '0019_task_overlap'), ('tasks', '0020_review'), ('tasks', '0021_auto_20200417_1019'), ('tasks', '0022_taskcompletion_result_count'), ('tasks', '0023_storagelink'), ('tasks', '0024_auto_20200705_1436'), ('tasks', '0025_taskcompletionhistory'), ('tasks', '0026_remove_taskcompletion_updates_history'), ('tasks', '0027_taskcompletion_draft'), ('tasks', '0028_auto_20200814_1514'), ('tasks', '0029_auto_20200904_2035'), ('tasks', '0030_auto_20200904_2043'), ('tasks', '0031_auto_20200910_1402'), ('tasks', '0032_auto_20200921_1921'), ('tasks', '0033_auto_20201005_1552'), ('tasks', '0034_auto_20201203_1113'), ('tasks', '0035_remove_experts'), ('tasks', '0036_auto_20210121_1524'), ('tasks', '0036_auto_20210119_1144'), ('tasks', '0037_merge_20210126_1328'), ('tasks', '0038_delete_storagelink'), ('tasks', '0039_task_file_upload'), ('tasks', '0035_tasklock'), ('tasks', '0039_merge_20210222_1244'), ('tasks', '0040_merge_20210225_1126'), ('tasks', '0041_taskcompletionhistory_was_cancelled')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_import', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(help_text='User uploaded data for the task. Data is formatted corresponding to the project label config. Examples of data for your project can be found at Upload Dialog on Data Manager page', verbose_name='data')),
                ('accuracy', models.FloatField(default=None, help_text='Completion agreement among experts', null=True, verbose_name='accuracy')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Task creation time', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Task last update time', verbose_name='updated at')),
                ('is_labeled', models.BooleanField(default=False, help_text='True if the completion number for this task is greater or equal to the project maximum_completions', verbose_name='is_labeled')),
                ('project', models.ForeignKey(help_text='Project id for this task', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.project')),
                ('meta', models.JSONField(default=dict, help_text='Meta is a user uploaded data and it can be useful as MLBackend input (embeddings, advanced vectors, other info). It will be passed to ML while training/predict steps', null=True, verbose_name='meta')),
            ],
            options={
                'db_table': 'task',
                'ordering': ['-accuracy', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.JSONField(default=dict, null=True, verbose_name='result')),
                ('score', models.FloatField(default=0.0, verbose_name='score')),
                ('model_version', models.TextField(blank=True, default='', null=True, verbose_name='model version')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='tasks.task')),
                ('cluster', models.IntegerField(default=None, help_text='Cluster for the current prediction', null=True, verbose_name='cluster')),
            ],
            options={
                'db_table': 'prediction',
            },
        ),
        migrations.CreateModel(
            name='TaskCompletion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.JSONField(default=dict, help_text='Editor state (system data)', null=True, verbose_name='state')),
                ('result', models.JSONField(default=list, help_text='The main value of expert work - labeling result in JSON format', null=True, verbose_name='result')),
                ('was_cancelled', models.BooleanField(default=False, help_text='Expert skipped the task', verbose_name='was cancelled')),
                ('honeypot', models.BooleanField(default=False, help_text='This completion is Ground Truth (honeypot)', verbose_name='honeypot')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last update time', verbose_name='updated at')),
                ('completed_by', models.ForeignKey(help_text='User who made this completion', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completions', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(help_text='Corresponding task for this completion', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completions', to='tasks.task')),
                ('prediction', models.JSONField(default=dict, help_text='Prediction viewed at the time of completion', null=True, verbose_name='prediction')),
                ('prediction_equal_score', models.FloatField(default=0.0, help_text='Comparison result with prediction viewed at the time of completion', verbose_name='prediction_equal_score')),
                ('updates_history', models.JSONField(default=list, help_text='Updates history by experts', null=True, verbose_name='update history')),
            ],
            options={
                'db_table': 'task_completion',
            },
        ),
        migrations.AddField(
            model_name='prediction',
            name='ground_truth_match',
            field=models.FloatField(blank=True, default=None, help_text='Ground truth matching score if related task has ground truth', null=True, verbose_name='ground_truth_match'),
        ),
        migrations.AddField(
            model_name='prediction',
            name='neighbors',
            field=models.JSONField(blank=True, default=list, help_text='Array task IDs of the closest neighbors', null=True, verbose_name='neighbors'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='result',
            field=models.JSONField(default=dict, help_text='Prediction result', null=True, verbose_name='result'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='score',
            field=models.FloatField(default=0.0, help_text='Prediction score', verbose_name='score'),
        ),
        migrations.AddField(
            model_name='taskcompletion',
            name='lead_time',
            field=models.FloatField(default=None, help_text='how much time spent to solve the completion', null=True, verbose_name='lead time'),
        ),
        migrations.CreateModel(
            name='CompletionPairwiseStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matching_score', models.FloatField(default=0.0, help_text='Matching score', verbose_name='matching score')),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_pairwise_stats', to='tasks.taskcompletion')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_pairwise_stats', to='tasks.taskcompletion')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='taken_at',
            field=models.DateTimeField(blank=True, help_text='Time when task has been taken in work', null=True, verbose_name='taken_at'),
        ),
        migrations.AddField(
            model_name='prediction',
            name='mislabeling',
            field=models.FloatField(default=0.0, help_text='Related task mislabeling score', verbose_name='mislabeling'),
        ),
        migrations.AlterField(
            model_name='task',
            name='data',
            field=models.JSONField(help_text='User imported (uploaded) data for the task. Data is formatted corresponding to the project label config. Examples of data for your project can be found at Import Dialog on Data Manager page', verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='task',
            name='meta',
            field=models.JSONField(default=dict, help_text='Meta is a user imported (uploaded) data and it can be useful as MLBackend input(embeddings, advanced vectors, other info). It will be passed to ML while training/predict steps', null=True, verbose_name='meta'),
        ),
        migrations.AlterField(
            model_name='taskcompletion',
            name='completed_by',
            field=models.ForeignKey(help_text='Expert ID who made this completion', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='overlap',
            field=models.IntegerField(default=1, help_text='Number of distinct annotators which process current task', verbose_name='overlap'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('result', models.FloatField(default=0.0, help_text='Review result from -1.0 to 1.0', verbose_name='result')),
                ('completed_by', models.ForeignKey(help_text='Expert ID who made this completion', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('completion', models.ForeignKey(help_text='Completion review by users', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tasks.taskcompletion')),
            ],
        ),
        migrations.AddField(
            model_name='taskcompletion',
            name='result_count',
            field=models.IntegerField(default=0, help_text='Results inside of completion counter', verbose_name='result count'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='score',
            field=models.FloatField(default=0.0, help_text='Prediction score', null=True, verbose_name='score'),
        ),
        migrations.RemoveField(
            model_name='taskcompletion',
            name='updates_history',
        ),
        migrations.AddField(
            model_name='taskcompletion',
            name='draft',
            field=models.JSONField(default=None, help_text='Autosave during labeling', null=True, verbose_name='draft'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['project', 'is_labeled'], name='task_project_6acf5f_idx'),
        ),
        migrations.AddIndex(
            model_name='taskcompletion',
            index=models.Index(fields=['task', 'honeypot'], name='task_comple_task_id_07c6ca_idx'),
        ),
        migrations.AlterField(
            model_name='task',
            name='overlap',
            field=models.IntegerField(db_index=True, default=1, help_text='Number of distinct annotators which process current task', verbose_name='overlap'),
        ),
        migrations.AlterField(
            model_name='taskcompletion',
            name='result',
            field=models.JSONField(default=None, help_text='The main value of expert work - labeling result in JSON format', null=True, verbose_name='result'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['id', 'overlap'], name='task_id_7a9aca_idx'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='score',
            field=models.FloatField(default=None, help_text='Prediction score', null=True, verbose_name='score'),
        ),
        migrations.CreateModel(
            name='TaskCompletionDraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.JSONField(help_text='Draft result in JSON format', verbose_name='result')),
                ('lead_time', models.FloatField(help_text='how much time spent to solve the completion', verbose_name='lead time')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last update time', verbose_name='updated at')),
            ],
        ),
        migrations.RemoveField(
            model_name='taskcompletion',
            name='draft',
        ),
        migrations.DeleteModel(
            name='CompletionPairwiseStats',
        ),
        migrations.AddField(
            model_name='taskcompletiondraft',
            name='completion',
            field=models.ForeignKey(blank=True, help_text='Corresponding completion for this draft', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drafts', to='tasks.taskcompletion'),
        ),
        migrations.AddField(
            model_name='taskcompletiondraft',
            name='task',
            field=models.ForeignKey(blank=True, help_text='Corresponding task for this draft', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drafts', to='tasks.task'),
        ),
        migrations.AddField(
            model_name='taskcompletiondraft',
            name='user',
            field=models.ForeignKey(help_text='User who made this draft', on_delete=django.db.models.deletion.CASCADE, related_name='drafts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RenameField(
            model_name='review',
            old_name='completed_by',
            new_name='completed_by_old',
        ),
        migrations.RenameField(
            model_name='taskcompletion',
            old_name='completed_by',
            new_name='completed_by_old',
        ),
        migrations.AddField(
            model_name='review',
            name='completed_by',
            field=models.ForeignKey(help_text='User ID who made this review', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taskcompletion',
            name='completed_by',
            field=models.ForeignKey(help_text='User ID who made this completion', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='review',
            name='completed_by_old',
        ),
        migrations.RemoveField(
            model_name='taskcompletion',
            name='completed_by_old',
        ),
        migrations.AlterField(
            model_name='task',
            name='accuracy',
            field=models.FloatField(default=None, help_text='Completion agreement among annotators', null=True, verbose_name='accuracy'),
        ),
        migrations.AlterField(
            model_name='taskcompletion',
            name='lead_time',
            field=models.FloatField(default=None, help_text='How much time spent to solve the completion', null=True, verbose_name='lead time'),
        ),
        migrations.AlterField(
            model_name='taskcompletion',
            name='result',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None, help_text='The main value of annotator work - labeling result in JSON format', null=True, verbose_name='result'),
        ),
        migrations.AlterField(
            model_name='taskcompletion',
            name='was_cancelled',
            field=models.BooleanField(default=False, help_text='User skipped the task', verbose_name='was cancelled'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='neighbors',
            field=models.JSONField(blank=True, help_text='Array task IDs of the closest neighbors', null=True, verbose_name='neighbors'),
        ),
        migrations.AlterField(
            model_name='taskcompletion',
            name='result',
            field=models.JSONField(default=None, help_text='The main value of annotator work - labeling result in JSON format', null=True, verbose_name='result'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='neighbors',
            field=models.JSONField(blank=True, help_text='Array task IDs of the closest neighbors', null=True, verbose_name='neighbors'),
        ),
        migrations.AlterField(
            model_name='taskcompletion',
            name='result',
            field=models.JSONField(default=None, help_text='The main value of annotator work - labeling result in JSON format', null=True, verbose_name='result'),
        ),
        migrations.AddField(
            model_name='task',
            name='file_upload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='data_import.fileupload'),
        ),
        migrations.CreateModel(
            name='TaskLock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_at', models.DateTimeField(verbose_name='expire_at')),
                ('task', models.ForeignKey(help_text='Locked task', on_delete=django.db.models.deletion.CASCADE, related_name='locks', to='tasks.task')),
                ('user', models.ForeignKey(help_text='User who made this task lock', on_delete=django.db.models.deletion.CASCADE, related_name='task_locks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
