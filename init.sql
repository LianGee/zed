create table album
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
  on album (created_at);

create index idx_is_delete
  on album (is_delete);

create index idx_updated_at
  on album (updated_at);

create index idx_user_name
  on album (user_name);

create table article
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
  on article (catalogue_id);

create index idk_file_key
  on article (file_key);

create index idk_is_published
  on article (is_published);

create index idk_user_name
  on article (user_name);

create index idx_created_at
  on article (created_at);

create index idx_is_delete
  on article (is_delete);

create index idx_updated_at
  on article (updated_at);

create table catalogue
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
  on catalogue (user_name);

create index idx_created_at
  on catalogue (created_at);

create index idx_is_delete
  on catalogue (is_delete);

create index idx_updated_at
  on catalogue (updated_at);

create table graph
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
  on graph (type);

create index idx_created_at
  on graph (created_at);

create index idx_format
  on graph (format);

create index idx_img_key
  on graph (img_key);

create index idx_is_delete
  on graph (is_delete);

create index idx_is_published
  on graph (is_published);

create index idx_updated_at
  on graph (updated_at);

create index idx_user_name
  on graph (user_name);

create table image
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
  on image (album_id);

create index idk_user_name
  on image (user_name);

create index idx_created_at
  on image (created_at);

create index idx_is_delete
  on image (is_delete);

create index idx_key
  on image (`key`);

create index idx_updated_at
  on image (updated_at);

create table tag
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
  on tag (created_at);

create index idx_is_delete
  on tag (is_delete);

create index idx_label
  on tag (label);

create index idx_updated_at
  on tag (updated_at);

create index idx_user_name
  on tag (user_name);

create table user
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
  on user (created_at);

create index idx_is_delete
  on user (is_delete);

create index idx_updated_at
  on user (updated_at);

create table user_like
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
  on user_like (article_id);

create index idx_comment_id
  on user_like (comment_id);

create index idx_created_at
  on user_like (created_at);

create index idx_is_delete
  on user_like (is_delete);

create index idx_updated_at
  on user_like (updated_at);

create index idx_user_name
  on user_like (user_name);

create table user_view
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
  on user_view (article_id);

create index idx_created_at
  on user_view (created_at);

create index idx_is_delete
  on user_view (is_delete);

create index idx_updated_at
  on user_view (updated_at);

create index idx_user_name
  on user_view (user_name);

