#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple

from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm, IntPrompt

console = Console()

# 支持的图片文件扩展名
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.ico'}


def get_file_info(file_path: Path) -> Tuple[str, datetime, int]:
    """获取文件信息：路径、创建时间、文件大小"""
    stat = file_path.stat()
    # 使用修改时间作为创建时间（在某些系统上更可靠）
    creation_time = datetime.fromtimestamp(stat.st_mtime)
    size_kb = stat.st_size / 1024  # 转换为KB
    return str(file_path), creation_time, int(size_kb)


def find_images(directory: str = '.') -> List[Path]:
    """遍历目录及子目录，找到所有图片文件"""
    images = []
    directory_path = Path(directory)

    console.print(f"[blue]正在扫描目录: {directory_path.absolute()}[/blue]")

    for file_path in directory_path.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in IMAGE_EXTENSIONS:
            images.append(file_path)

    console.print(f"[green]找到 {len(images)} 个图片文件[/green]")
    return images


def filter_images(images: List[Path], days_before: int, min_size_kb: int) -> List[Tuple[str, datetime, int]]:
    """根据条件筛选图片"""
    cutoff_date = datetime.now() - timedelta(days=days_before)
    filtered_images = []

    console.print(f"[blue]筛选条件: 创建于 {days_before} 天前({cutoff_date.strftime('%Y-%m-%d %H:%M:%S')})，大小 > {min_size_kb} KB[/blue]")

    for image in images:
        try:
            path_str, creation_time, size_kb = get_file_info(image)

            # 检查是否符合条件
            if creation_time < cutoff_date and size_kb > min_size_kb:
                filtered_images.append((path_str, creation_time, size_kb))

        except (OSError, ValueError) as e:
            console.print(f"[red]无法读取文件信息: {image} - {e}[/red]")
            continue

    return filtered_images


def display_results(filtered_images: List[Tuple[str, datetime, int]]):
    """使用rich表格显示结果"""
    if not filtered_images:
        console.print("[yellow]没有找到符合条件的图片文件[/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("序号", justify="right", style="cyan", width=6)
    table.add_column("文件路径", style="green")
    table.add_column("创建时间", justify="center", style="yellow", width=20)
    table.add_column("文件大小(KB)", justify="right", style="red", width=15)

    total_size = 0
    for i, (path, creation_time, size_kb) in enumerate(filtered_images, 1):
        table.add_row(
            str(i),
            path,
            creation_time.strftime('%Y-%m-%d %H:%M:%S'),
            f"{size_kb:,}"
        )
        total_size += size_kb

    console.print(table)
    console.print(f"\n[bold]总计: {len(filtered_images)} 个文件，总大小: {total_size:,} KB ({total_size / 1024:.2f} MB)[/bold]")


def delete_files(file_paths: List[str]) -> int:
    """删除文件并返回成功删除的数量"""
    success_count = 0

    with console.status("[bold green]正在删除文件...") as status:
        for i, file_path in enumerate(file_paths, 1):
            try:
                os.remove(file_path)
                console.print(f"[green]✓ 已删除: {file_path}[/green]")
                success_count += 1
            except OSError as e:
                console.print(f"[red]✗ 删除失败: {file_path} - {e}[/red]")

            status.update(f"[bold green]正在删除文件... ({i}/{len(file_paths)})")

    return success_count


def main():
    console.print("[bold blue]图片文件清理工具[/bold blue]\n")

    # 获取用户输入
    try:
        days_before = IntPrompt.ask("请输入天数（筛选多少天前创建的文件）", default=30)
        min_size_kb = IntPrompt.ask("请输入最小文件大小（KB）", default=1000)

        if days_before < 0 or min_size_kb < 0:
            console.print("[red]天数和文件大小必须为正数[/red]")
            return

    except KeyboardInterrupt:
        console.print("\n[yellow]操作已取消[/yellow]")
        return

    # 查找所有图片文件
    try:
        images = find_images()
        if not images:
            console.print("[yellow]当前目录及子目录中没有找到图片文件[/yellow]")
            return

    except Exception as e:
        console.print(f"[red]扫描目录时出错: {e}[/red]")
        return

    # 筛选符合条件的图片
    filtered_images = filter_images(images, days_before, min_size_kb)

    # 显示结果
    display_results(filtered_images)

    # 如果有符合条件的文件，询问是否删除
    if filtered_images:
        console.print("\n[bold yellow]警告: 删除操作无法撤销![/bold yellow]")

        if Confirm.ask("确认要删除这些文件吗？", default=False):
            file_paths = [path for path, _, _ in filtered_images]
            success_count = delete_files(file_paths)

            console.print(f"\n[bold green]删除完成！成功删除 {success_count}/{len(file_paths)} 个文件[/bold green]")
        else:
            console.print("[yellow]操作已取消，没有删除任何文件[/yellow]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]程序已被用户中断[/yellow]")
    except Exception as e:
        console.print(f"\n[red]程序执行出错: {e}[/red]")
