create table if not exists zed.album
(
  id          bigint(11) auto_increment comment '主键'
    primary key,
  user_name   varchar(50) default '' not null comment '用户名',
  title       varchar(50) default '' not null comment '相册名',
  description text                   null comment '描述',
  cover_url   text                   null,
  is_public   tinyint(3)  default 0  not null,
  created_at  bigint(11)             null comment '创建时间',
  updated_at  bigint(11)             null comment '更新时间',
  is_delete   tinyint(3)  default 0  null comment '是否删除'
)
  comment '相册目录' charset = utf8mb4;

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
  id              bigint(11) auto_increment comment '主键'
    primary key,
  catalogue_id    bigint(11)    default 1    not null,
  catalogue_index bigint(11)    default 0    not null comment '在目录中的顺序',
  title           varchar(1024) default ''   null comment '标题',
  user_name       varchar(50)   default ''   not null comment '用户名',
  file_key        varchar(32)   default ''   null comment 'md5',
  url             varchar(1024) default ''   null comment '七牛路径',
  is_published    tinyint(3)    default 0    null comment '是否发布',
  tags            varchar(1024) default '[]' null comment 'tags',
  summary         varchar(500)  default ''   null comment '摘要',
  view_num        bigint(11)    default 0    not null comment '浏览量',
  like_num        bigint(11)    default 0    not null comment '点赞量',
  comment_num     bigint(11)    default 0    not null comment '评论数量',
  created_at      bigint(11)                 null comment '创建时间',
  updated_at      bigint(11)                 null comment '更新时间',
  is_delete       tinyint(3)    default 0    null comment '是否删除'
)
  comment '文章' charset = utf8mb4;

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
  id         bigint(11) auto_increment comment '主键'
    primary key,
  name       varchar(250) default '' not null comment '目录名',
  `index`    bigint(11)   default 0  not null,
  user_name  varchar(50)  default '' not null,
  created_at bigint(11)              null comment '创建时间',
  updated_at bigint(11)              null comment '更新时间',
  is_delete  tinyint(3)   default 0  null comment '是否删除'
)
  comment '目录' charset = utf8mb4;

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
  id           bigint(11) auto_increment comment '主键'
    primary key,
  title        varchar(1024) default ''     null comment '标题',
  user_name    varchar(50)   default ''     not null comment '用户名',
  type         varchar(5)    default 'flow' not null comment '图形类型',
  data_key     varchar(32)   default ''     not null comment '文件名',
  data_url     varchar(1024) default ''     not null comment '文件路径',
  img_key      varchar(32)   default ''     null comment '图片文件的key',
  img_url      varchar(1024) default ''     null comment '图片存储路径',
  width        bigint(11)    default 0      null comment '图片宽',
  height       bigint(11)    default 0      null comment '图高',
  size         bigint(11)    default 0      null,
  format       varchar(20)   default ''     null comment '文件类型',
  tags         varchar(1024) default '[]'   null comment '标签',
  color_model  varchar(20)   default ''     null comment '色彩模式',
  is_published tinyint(3)    default 0      not null comment '是否发布',
  created_at   bigint(11)                   null comment '创建时间',
  updated_at   bigint(11)                   null comment '更新时间',
  is_delete    tinyint(3)    default 0      null comment '是否删除',
  constraint uk_data_key
    unique (data_key)
)
  comment '图形' charset = utf8mb4;

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
  id          bigint(11) auto_increment comment '主键'
    primary key,
  album_id    bigint(11)    default 0  not null comment '相册id',
  user_name   varchar(50)   default '' not null comment '上传用户',
  `key`       varchar(32)   default '' not null,
  url         varchar(1024) default '' not null comment '图片url',
  size        bigint(11)    default 0  not null,
  format      varchar(50)   default '' not null,
  width       bigint(11)    default 0  not null,
  height      bigint(11)    default 0  not null,
  color_model varchar(50)   default '' not null comment '色彩模式',
  created_at  bigint(11)               null comment '创建时间',
  updated_at  bigint(11)               null comment '更新时间',
  is_delete   tinyint(3)    default 0  null comment '是否删除'
)
  comment '图片' charset = utf8mb4;

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
  id         bigint(11) auto_increment comment '主键'
    primary key,
  user_name  varchar(50)            null comment '创建者',
  label      varchar(50) default '' null comment '标签内容',
  created_at bigint(11)             null comment '创建时间',
  updated_at bigint(11)             null comment '更新时间',
  is_delete  tinyint(3)  default 0  null comment '是否删除'
)
  comment '标签' charset = utf8mb4;

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
  id         bigint(11) auto_increment comment '主键'
    primary key,
  name       varchar(50)   default ''                                                                               null comment '用户名',
  email      varchar(50)   default 'example@sse.com.cn'                                                             null comment '邮箱',
  phone      varchar(11)   default ''                                                                               null comment '电话号码',
  password   varchar(50)                                                                                            null comment '密码',
  avatar     varchar(1024) default 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png' null,
  created_at bigint(11)                                                                                             null comment '创建时间',
  updated_at bigint(11)                                                                                             null comment '更新时间',
  is_delete  tinyint(3)    default 0                                                                                null comment '是否删除',
  constraint uk_name
    unique (name)
)
  comment '用户' charset = utf8mb4;

create index idx_created_at
  on zed.user (created_at);

create index idx_is_delete
  on zed.user (is_delete);

create index idx_updated_at
  on zed.user (updated_at);

create table if not exists zed.user_like
(
  id         bigint(11) auto_increment comment '主键'
    primary key,
  user_name  varchar(50) default '' not null comment '用户名',
  article_id bigint(11)  default 0  null comment '文章id',
  comment_id bigint(11)  default 0  null comment '评论id',
  liked      tinyint(3)  default 0  not null comment '0 否 1 是',
  created_at bigint(11)             null comment '创建时间',
  updated_at bigint(11)             null comment '更新时间',
  is_delete  tinyint(3)  default 0  null comment '是否删除'
)
  comment '用户点赞' charset = utf8mb4;

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
  id         bigint(11) auto_increment comment '主键'
    primary key,
  user_name  varchar(50) default '' not null comment '用户名',
  article_id bigint(11)  default 0  null comment '文章ID',
  created_at bigint(11)             null comment '创建时间',
  updated_at bigint(11)             null comment '更新时间',
  is_delete  tinyint(3)  default 0  null comment '是否删除'
)
  comment '用户浏览记录' charset = utf8mb4;

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
  id           bigint(11) auto_increment comment '主键'
    primary key,
  user_name    varchar(50)   default '' not null comment '用户名',
  workspace_id bigint(11)    default 0  not null comment '空间',
  title        varchar(1024) default '' not null,
  created_at   bigint(11)               null comment '创建时间',
  updated_at   bigint(11)               null comment '更新时间',
  is_delete    tinyint(3)    default 0  null comment '是否删除'
)
  comment '星期计划' charset = utf8mb4;

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
  id         bigint(11) auto_increment comment '主键'
    primary key,
  planner_id bigint(11)  default 0  not null,
  task_index tinyint(3)  default 0  null comment '星期几',
  user_name  varchar(50) default '' not null comment '用户名',
  content    text                   null comment '任务内容',
  status     tinyint(3)  default 0  not null comment '任务状态',
  start      bigint(11)  default 0  null comment '开始时间',
  end        bigint(11)  default 0  not null comment '结束时间',
  created_at bigint(11)             null comment '创建时间',
  updated_at bigint(11)             null comment '更新时间',
  is_delete  tinyint(3)  default 0  null comment '是否删除'
)
  comment '星期计划' charset = utf8mb4;

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
  id         bigint(11) auto_increment comment '主键'
    primary key,
  user_name  varchar(50)  default '' not null comment '用户名',
  name       varchar(250) default '' not null comment '空间名',
  created_at bigint(11)              null comment '创建时间',
  updated_at bigint(11)              null comment '更新时间',
  is_delete  tinyint(3)   default 0  null comment '是否删除'
)
  comment '工作间' charset = utf8mb4;

create index idx_created_at
  on zed.workspace (created_at);

create index idx_is_delete
  on zed.workspace (is_delete);

create index idx_updated_at
  on zed.workspace (updated_at);

create index idx_user_name
  on zed.workspace (user_name);

