create table if not exists zed.album
(
  id          bigint(11) auto_increment comment '����'
    primary key,
  user_name   varchar(50) default '' not null comment '�û���',
  title       varchar(50) default '' not null comment '�����',
  description text                   null comment '����',
  cover_url   text                   null,
  is_public   tinyint(3)  default 0  not null,
  created_at  bigint(11)             null comment '����ʱ��',
  updated_at  bigint(11)             null comment '����ʱ��',
  is_delete   tinyint(3)  default 0  null comment '�Ƿ�ɾ��'
)
  comment '���Ŀ¼' charset = utf8mb4;

create index idx_created_at
  on zed.album (created_at);

create index idx_is_delete
  on zed.album (is_delete);

create index idx_updated_at
  on zed.album (updated_at);

create index idx_user_name
  on zed.album (user_name);

create table if not exists zed.article
(
  id              bigint(11) auto_increment comment '����'
    primary key,
  catalogue_id    bigint(11)    default 1    not null,
  catalogue_index bigint(11)    default 0    not null comment '��Ŀ¼�е�˳��',
  title           varchar(1024) default ''   null comment '����',
  user_name       varchar(50)   default ''   not null comment '�û���',
  file_key        varchar(32)   default ''   null comment 'md5',
  url             varchar(1024) default ''   null comment '��ţ·��',
  is_published    tinyint(3)    default 0    null comment '�Ƿ񷢲�',
  tags            varchar(1024) default '[]' null comment 'tags',
  summary         varchar(500)  default ''   null comment 'ժҪ',
  view_num        bigint(11)    default 0    not null comment '�����',
  like_num        bigint(11)    default 0    not null comment '������',
  comment_num     bigint(11)    default 0    not null comment '��������',
  created_at      bigint(11)                 null comment '����ʱ��',
  updated_at      bigint(11)                 null comment '����ʱ��',
  is_delete       tinyint(3)    default 0    null comment '�Ƿ�ɾ��'
)
  comment '����' charset = utf8mb4;

create index idk_catalogue_id
  on zed.article (catalogue_id);

create index idk_file_key
  on zed.article (file_key);

create index idk_is_published
  on zed.article (is_published);

create index idk_user_name
  on zed.article (user_name);

create index idx_created_at
  on zed.article (created_at);

create index idx_is_delete
  on zed.article (is_delete);

create index idx_updated_at
  on zed.article (updated_at);

create table if not exists zed.catalogue
(
  id         bigint(11) auto_increment comment '����'
    primary key,
  name       varchar(250) default '' not null comment 'Ŀ¼��',
  `index`    bigint(11)   default 0  not null,
  user_name  varchar(50)  default '' not null,
  created_at bigint(11)              null comment '����ʱ��',
  updated_at bigint(11)              null comment '����ʱ��',
  is_delete  tinyint(3)   default 0  null comment '�Ƿ�ɾ��'
)
  comment 'Ŀ¼' charset = utf8mb4;

create index idk_user_name
  on zed.catalogue (user_name);

create index idx_created_at
  on zed.catalogue (created_at);

create index idx_is_delete
  on zed.catalogue (is_delete);

create index idx_updated_at
  on zed.catalogue (updated_at);

create table if not exists zed.graph
(
  id           bigint(11) auto_increment comment '����'
    primary key,
  title        varchar(1024) default ''     null comment '����',
  user_name    varchar(50)   default ''     not null comment '�û���',
  type         varchar(5)    default 'flow' not null comment 'ͼ������',
  data_key     varchar(32)   default ''     not null comment '�ļ���',
  data_url     varchar(1024) default ''     not null comment '�ļ�·��',
  img_key      varchar(32)   default ''     null comment 'ͼƬ�ļ���key',
  img_url      varchar(1024) default ''     null comment 'ͼƬ�洢·��',
  width        bigint(11)    default 0      null comment 'ͼƬ��',
  height       bigint(11)    default 0      null comment 'ͼ��',
  size         bigint(11)    default 0      null,
  format       varchar(20)   default ''     null comment '�ļ�����',
  tags         varchar(1024) default '[]'   null comment '��ǩ',
  color_model  varchar(20)   default ''     null comment 'ɫ��ģʽ',
  is_published tinyint(3)    default 0      not null comment '�Ƿ񷢲�',
  created_at   bigint(11)                   null comment '����ʱ��',
  updated_at   bigint(11)                   null comment '����ʱ��',
  is_delete    tinyint(3)    default 0      null comment '�Ƿ�ɾ��',
  constraint uk_data_key
    unique (data_key)
)
  comment 'ͼ��' charset = utf8mb4;

create index idk_type
  on zed.graph (type);

create index idx_created_at
  on zed.graph (created_at);

create index idx_format
  on zed.graph (format);

create index idx_img_key
  on zed.graph (img_key);

create index idx_is_delete
  on zed.graph (is_delete);

create index idx_is_published
  on zed.graph (is_published);

create index idx_updated_at
  on zed.graph (updated_at);

create index idx_user_name
  on zed.graph (user_name);

create table if not exists zed.image
(
  id          bigint(11) auto_increment comment '����'
    primary key,
  album_id    bigint(11)    default 0  not null comment '���id',
  user_name   varchar(50)   default '' not null comment '�ϴ��û�',
  `key`       varchar(32)   default '' not null,
  url         varchar(1024) default '' not null comment 'ͼƬurl',
  size        bigint(11)    default 0  not null,
  format      varchar(50)   default '' not null,
  width       bigint(11)    default 0  not null,
  height      bigint(11)    default 0  not null,
  color_model varchar(50)   default '' not null comment 'ɫ��ģʽ',
  created_at  bigint(11)               null comment '����ʱ��',
  updated_at  bigint(11)               null comment '����ʱ��',
  is_delete   tinyint(3)    default 0  null comment '�Ƿ�ɾ��'
)
  comment 'ͼƬ' charset = utf8mb4;

create index idk_album_id
  on zed.image (album_id);

create index idk_user_name
  on zed.image (user_name);

create index idx_created_at
  on zed.image (created_at);

create index idx_is_delete
  on zed.image (is_delete);

create index idx_key
  on zed.image (`key`);

create index idx_updated_at
  on zed.image (updated_at);

create table if not exists zed.tag
(
  id         bigint(11) auto_increment comment '����'
    primary key,
  user_name  varchar(50)            null comment '������',
  label      varchar(50) default '' null comment '��ǩ����',
  created_at bigint(11)             null comment '����ʱ��',
  updated_at bigint(11)             null comment '����ʱ��',
  is_delete  tinyint(3)  default 0  null comment '�Ƿ�ɾ��'
)
  comment '��ǩ' charset = utf8mb4;

create index idx_created_at
  on zed.tag (created_at);

create index idx_is_delete
  on zed.tag (is_delete);

create index idx_label
  on zed.tag (label);

create index idx_updated_at
  on zed.tag (updated_at);

create index idx_user_name
  on zed.tag (user_name);

create table if not exists zed.user
(
  id         bigint(11) auto_increment comment '����'
    primary key,
  name       varchar(50)   default ''                                                                               null comment '�û���',
  email      varchar(50)   default 'example@sse.com.cn'                                                             null comment '����',
  phone      varchar(11)   default ''                                                                               null comment '�绰����',
  password   varchar(50)                                                                                            null comment '����',
  avatar     varchar(1024) default 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png' null,
  created_at bigint(11)                                                                                             null comment '����ʱ��',
  updated_at bigint(11)                                                                                             null comment '����ʱ��',
  is_delete  tinyint(3)    default 0                                                                                null comment '�Ƿ�ɾ��',
  constraint uk_name
    unique (name)
)
  comment '�û�' charset = utf8mb4;

create index idx_created_at
  on zed.user (created_at);

create index idx_is_delete
  on zed.user (is_delete);

create index idx_updated_at
  on zed.user (updated_at);

create table if not exists zed.user_like
(
  id         bigint(11) auto_increment comment '����'
    primary key,
  user_name  varchar(50) default '' not null comment '�û���',
  article_id bigint(11)  default 0  null comment '����id',
  comment_id bigint(11)  default 0  null comment '����id',
  liked      tinyint(3)  default 0  not null comment '0 �� 1 ��',
  created_at bigint(11)             null comment '����ʱ��',
  updated_at bigint(11)             null comment '����ʱ��',
  is_delete  tinyint(3)  default 0  null comment '�Ƿ�ɾ��'
)
  comment '�û�����' charset = utf8mb4;

create index idx_article_id
  on zed.user_like (article_id);

create index idx_comment_id
  on zed.user_like (comment_id);

create index idx_created_at
  on zed.user_like (created_at);

create index idx_is_delete
  on zed.user_like (is_delete);

create index idx_updated_at
  on zed.user_like (updated_at);

create index idx_user_name
  on zed.user_like (user_name);

create table if not exists zed.user_view
(
  id         bigint(11) auto_increment comment '����'
    primary key,
  user_name  varchar(50) default '' not null comment '�û���',
  article_id bigint(11)  default 0  null comment '����ID',
  created_at bigint(11)             null comment '����ʱ��',
  updated_at bigint(11)             null comment '����ʱ��',
  is_delete  tinyint(3)  default 0  null comment '�Ƿ�ɾ��'
)
  comment '�û������¼' charset = utf8mb4;

create index idk_article_id
  on zed.user_view (article_id);

create index idx_created_at
  on zed.user_view (created_at);

create index idx_is_delete
  on zed.user_view (is_delete);

create index idx_updated_at
  on zed.user_view (updated_at);

create index idx_user_name
  on zed.user_view (user_name);

create table if not exists zed.weekly_planner
(
  id           bigint(11) auto_increment comment '����'
    primary key,
  user_name    varchar(50)   default '' not null comment '�û���',
  workspace_id bigint(11)    default 0  not null comment '�ռ�',
  title        varchar(1024) default '' not null,
  created_at   bigint(11)               null comment '����ʱ��',
  updated_at   bigint(11)               null comment '����ʱ��',
  is_delete    tinyint(3)    default 0  null comment '�Ƿ�ɾ��'
)
  comment '���ڼƻ�' charset = utf8mb4;

create index idk_workspace_id
  on zed.weekly_planner (workspace_id);

create index idx_created_at
  on zed.weekly_planner (created_at);

create index idx_is_delete
  on zed.weekly_planner (is_delete);

create index idx_updated_at
  on zed.weekly_planner (updated_at);

create index idx_user_name
  on zed.weekly_planner (user_name);

create table if not exists zed.weekly_task
(
  id         bigint(11) auto_increment comment '����'
    primary key,
  planner_id bigint(11)  default 0  not null,
  task_index tinyint(3)  default 0  null comment '���ڼ�',
  user_name  varchar(50) default '' not null comment '�û���',
  content    text                   null comment '��������',
  status     tinyint(3)  default 0  not null comment '����״̬',
  start      bigint(11)  default 0  null comment '��ʼʱ��',
  end        bigint(11)  default 0  not null comment '����ʱ��',
  created_at bigint(11)             null comment '����ʱ��',
  updated_at bigint(11)             null comment '����ʱ��',
  is_delete  tinyint(3)  default 0  null comment '�Ƿ�ɾ��'
)
  comment '���ڼƻ�' charset = utf8mb4;

create index idk_end
  on zed.weekly_task (end);

create index idk_start
  on zed.weekly_task (start);

create index idx_created_at
  on zed.weekly_task (created_at);

create index idx_is_delete
  on zed.weekly_task (is_delete);

create index idx_planner_Id
  on zed.weekly_task (planner_id);

create index idx_updated_at
  on zed.weekly_task (updated_at);

create index idx_user_name
  on zed.weekly_task (user_name);

create table if not exists zed.workspace
(
  id         bigint(11) auto_increment comment '����'
    primary key,
  user_name  varchar(50)  default '' not null comment '�û���',
  name       varchar(250) default '' not null comment '�ռ���',
  created_at bigint(11)              null comment '����ʱ��',
  updated_at bigint(11)              null comment '����ʱ��',
  is_delete  tinyint(3)   default 0  null comment '�Ƿ�ɾ��'
)
  comment '������' charset = utf8mb4;

create index idx_created_at
  on zed.workspace (created_at);

create index idx_is_delete
  on zed.workspace (is_delete);

create index idx_updated_at
  on zed.workspace (updated_at);

create index idx_user_name
  on zed.workspace (user_name);

